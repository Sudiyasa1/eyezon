#!/usr/bin/env python3
"""mint_check — the safety questions worth asking before you ape.

    python3 mint_check.py <MINT_ADDRESS> [--rpc https://your-rpc]

Answers, from public chain data only:

  • Can the creator still mint more supply?      (mint authority)
  • Can the creator freeze your tokens?          (freeze authority)
  • How much supply do the top holders control?  (largest accounts)

None of this needs an EyezOn account, an API key, or our engine. It is the
cheap, boring check that catches the obvious traps — the ones that are fully
visible on chain and still catch people every day.

Exit codes:  0 clean  ·  1 risk flagged  ·  2 could not determine

⚠️ A clean result is NOT a green light. It says these specific traps are absent,
nothing more. A token can pass every check here and still go to zero — most do.
This tool narrows the question; it does not answer it.
"""
import argparse
import json
import sys
import urllib.error
import urllib.request

DEFAULT_RPC = "https://api.mainnet-beta.solana.com"
# The SPL Token program. A mint account is owned by this.
SPL_TOKEN = "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
SPL_TOKEN_2022 = "TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb"


def rpc(url, method, params):
    body = json.dumps({"jsonrpc": "2.0", "id": 1,
                       "method": method, "params": params}).encode()
    req = urllib.request.Request(
        url, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read())


def check(mint, url):
    """Returns (verdict, [findings]). Never guesses: an unreachable RPC is
    UNKNOWN, never 'clean' — a check you could not run is not a check that
    passed."""
    findings = []
    try:
        info = rpc(url, "getAccountInfo", [mint, {"encoding": "jsonParsed"}])
        val = ((info.get("result") or {}).get("value")) or None
        if not val:
            return "unknown", ["no account found at that address"]
        owner = val.get("owner")
        if owner not in (SPL_TOKEN, SPL_TOKEN_2022):
            return "unknown", ["not an SPL mint (owner %s)" % owner]

        parsed = (((val.get("data") or {}).get("parsed") or {}).get("info")) or {}
        mint_auth = parsed.get("mintAuthority")
        freeze_auth = parsed.get("freezeAuthority")
        decimals = parsed.get("decimals")
        supply = parsed.get("supply")

        if mint_auth:
            findings.append("RISK  mint authority is still live (%s…) — more "
                            "supply can be printed" % str(mint_auth)[:8])
        else:
            findings.append("ok    mint authority revoked — supply is fixed")

        if freeze_auth:
            findings.append("RISK  freeze authority is still live (%s…) — your "
                            "tokens can be frozen" % str(freeze_auth)[:8])
        else:
            findings.append("ok    freeze authority revoked")

        # Concentration: the top 20 token accounts as a share of supply.
        try:
            la = rpc(url, "getTokenLargestAccounts", [mint])
            holders = ((la.get("result") or {}).get("value")) or []
            total = float(supply or 0)
            if total > 0 and holders:
                top10 = sum(float(h.get("amount") or 0) for h in holders[:10])
                pct = 100.0 * top10 / total
                label = "RISK " if pct >= 50 else ("warn " if pct >= 30 else "ok   ")
                findings.append("%s top 10 accounts hold %.1f%% of supply"
                                % (label, pct))
            else:
                findings.append("?     holder concentration UNKNOWN "
                                "(no accounts returned)")
        except Exception as e:
            findings.append("?     holder concentration UNKNOWN (%s)"
                            % type(e).__name__)

        if decimals is not None:
            findings.append("info  decimals %s" % decimals)

        risky = any(f.startswith("RISK") for f in findings)
        return ("risk" if risky else "clean"), findings

    except urllib.error.URLError as e:
        msg = str(e)
        if "CERTIFICATE_VERIFY_FAILED" in msg:
            return "unknown", ["TLS certificate verification failed — a local "
                              "Python cert-store problem, not a bad address. On "
                              "macOS run 'Install Certificates.command', or pass "
                              "--rpc for an endpoint you can reach."]
        return "unknown", ["RPC unreachable (%s)" % type(e).__name__]
    except Exception as e:
        return "unknown", ["could not determine (%s)" % type(e).__name__]


def main():
    ap = argparse.ArgumentParser(description="Pre-ape safety check for a Solana mint.")
    ap.add_argument("mint")
    ap.add_argument("--rpc", default=DEFAULT_RPC,
                    help="RPC endpoint (default: public mainnet, rate-limited)")
    a = ap.parse_args()

    verdict, findings = check(a.mint, a.rpc)
    icon = {"clean": "✅", "risk": "🚩", "unknown": "❓"}[verdict]
    print("%s %s" % (icon, verdict.upper()))
    for f in findings:
        print("   %s" % f)
    if verdict == "clean":
        print("\n   Clean here means these traps are absent — not that it is a "
              "good trade.")
    return {"clean": 0, "risk": 1, "unknown": 2}[verdict]


if __name__ == "__main__":
    sys.exit(main())
