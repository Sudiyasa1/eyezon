# mint-check

The boring questions worth asking before you ape.

```bash
python3 mint_check.py <MINT_ADDRESS> [--rpc https://your-rpc]
```

```
✅ CLEAN
   ok    mint authority revoked — supply is fixed
   ok    freeze authority revoked
   ok    top 10 accounts hold 17.3% of supply
   info  decimals 6
```

Exit codes: `0` clean · `1` risk flagged · `2` could not determine.

## What it checks

**Mint authority.** Still live means the creator can print more supply whenever
they like. Your bag gets diluted and there is nothing you can do.

**Freeze authority.** Still live means your tokens can be frozen in your own
wallet. You hold them; you just can't sell them.

**Concentration.** What share of supply the top ten accounts control. High
concentration isn't automatically a scam — but it means a handful of wallets
can end the chart whenever they choose.

All of it is public chain data. No API key, no account, no EyezOn dependency.

## What it does not do

A clean result means these specific traps are absent. It is not a green light,
and this tool will never tell you a token is good — that is a different and much
harder question. Narrow the field with it, then do the rest of your work.

**An unreachable RPC exits `2`, never `0`.** A check you could not run is not a
check that passed, and anything that blurs those two will eventually tell you a
loaded gun is empty.

Standard library only. Public mainnet RPC by default — pass `--rpc` for your own
if you're checking more than a couple.
