# pool-validator

One question: **is this Solana account actually a PumpSwap AMM pool?**

```bash
python3 pool_validator.py <ACCOUNT_ADDRESS> [--rpc https://your-rpc]
```

```
✅ POOL: PumpSwap AMM pool, 301 bytes
❌ NOT_POOL: SPL token account (a vault), 165 bytes — never returns a pool price
❓ UNKNOWN: RPC unreachable — cannot determine
```

Exit codes: `0` pool · `1` not a pool · `2` could not determine.

## Why it exists

A pump.fun graduation hands you an address. That address is not always the pool.

An SPL token vault and an AMM pool look similar enough to fool a naive check —
and asking a vault for a price gets you nothing, forever, while the token runs
without you. The distinction is one `getAccountInfo`: a vault is owned by the
SPL Token program and is 165 bytes; a PumpSwap pool is owned by `pAMMBay…` and
is ~300 bytes with a known discriminator.

One call, immediately, instead of retrying something that was never going to
answer. If you're building anything that reads pump.fun migrations, you want
this check in front of your pricing path.

## Design note

**An RPC failure exits `2`, never `1`.** "I could not check" is not "it is invalid".
Anything that collapses those two into one answer will eventually tell you a healthy
pool is broken, which is worse than telling you nothing.

No dependencies beyond the standard library. Defaults to public mainnet RPC; pass
`--rpc` for your own, which you will want for anything more than a spot check.
