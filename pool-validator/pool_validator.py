#!/usr/bin/env python3
"""Is this Solana account actually a PumpSwap AMM pool?

Built after a graduation event handed us an address that looked like a pool,
was stored as the pool, and was re-probed for 16 minutes. It was an
SPL token account — a vault. It was never going to return a price.

The check is one `getAccountInfo`:

  * owner must be the PumpSwap AMM program
  * data must carry the pool discriminator and be long enough to parse

A token account is owned by the SPL Token program and is 165 bytes. A real
PumpSwap pool is owned by pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA and is
~300 bytes. Telling them apart costs one RPC call; not telling them apart cost
us a quarter of an hour per token.

Usage:
    python3 pool_validator.py <ACCOUNT_ADDRESS> [--rpc URL]

Exit codes: 0 = is a pool · 1 = is not · 2 = could not determine (UNKNOWN).

⚖️ An RPC failure exits 2, never 1. "I could not check" is not "it is invalid".
"""
import argparse
import base64
import json
import sys
import urllib.error
import urllib.request

PUMPSWAP_PROGRAM_ID = "pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA"
SPL_TOKEN_PROGRAM_ID = "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
POOL_MIN_BYTES = 229          # 8-byte discriminator + 221 bytes of fields
DEFAULT_RPC = "https://api.mainnet-beta.solana.com"


def get_account(address, rpc):
    body = json.dumps({
        "jsonrpc": "2.0", "id": 1, "method": "getAccountInfo",
        "params": [address, {"encoding": "base64"}],
    }).encode()
    req = urllib.request.Request(rpc, data=body,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())


def classify(address, rpc=DEFAULT_RPC):
    """-> (verdict, detail). verdict is 'pool' | 'not_pool' | 'unknown'."""
    try:
        res = get_account(address, rpc)
    except (urllib.error.URLError, TimeoutError, ValueError) as e:
        msg = str(e)
        if "CERTIFICATE_VERIFY_FAILED" in msg:
            # Common on macOS when Python ships without a populated cert store.
            # Say what to do rather than leaving the user staring at an SSL trace.
            return "unknown", ("TLS certificate verification failed — this is a local Python "
                               "cert-store problem, not a bad address. On macOS run "
                               "'Install Certificates.command' in your Python folder, or use "
                               "an RPC you can reach.")
        return "unknown", f"RPC unreachable ({type(e).__name__}) — cannot determine"
    if "error" in res:
        return "unknown", f"RPC error: {res['error'].get('message', 'unknown')}"
    value = (res.get("result") or {}).get("value")
    if value is None:
        return "not_pool", "account does not exist on chain"
    owner = value.get("owner", "")
    try:
        raw = base64.b64decode(value["data"][0])
    except Exception:
        return "unknown", "account data not base64 — cannot inspect"
    size = len(raw)
    if owner == SPL_TOKEN_PROGRAM_ID:
        return "not_pool", f"SPL token account (a vault), {size} bytes — never returns a pool price"
    if owner != PUMPSWAP_PROGRAM_ID:
        return "not_pool", f"owned by {owner[:16]}…, not the PumpSwap AMM program ({size} bytes)"
    if size < POOL_MIN_BYTES:
        return "not_pool", f"owned by PumpSwap but only {size} bytes (< {POOL_MIN_BYTES}) — cannot be a pool"
    return "pool", f"PumpSwap AMM pool, {size} bytes"


def main():
    ap = argparse.ArgumentParser(description="Check whether an account is a PumpSwap AMM pool.")
    ap.add_argument("address")
    ap.add_argument("--rpc", default=DEFAULT_RPC, help="Solana RPC endpoint")
    a = ap.parse_args()
    verdict, detail = classify(a.address, a.rpc)
    icon = {"pool": "✅", "not_pool": "❌", "unknown": "❓"}[verdict]
    print(f"{icon} {verdict.upper()}: {detail}")
    return {"pool": 0, "not_pool": 1, "unknown": 2}[verdict]


if __name__ == "__main__":
    sys.exit(main())
