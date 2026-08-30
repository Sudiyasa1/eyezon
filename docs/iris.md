# IRIS — detection

IRIS is the layer that notices. It holds a live websocket subscription to
Solana and watches for the moment a pump.fun token completes its bonding curve
and its AMM pool is created on chain.

**Fastest observed: one second from block time to detection.**

## Coverage, and how we measure it

Coverage is **100%** of graduations since 16 July 2026 — and the number that
matters is what it is measured against.

Most systems measure coverage against a vendor: "we saw everything the API told
us about." That is circular. A feed that silently drops a migration makes you
look perfect while you miss it.

IRIS is measured against **chain truth** — migrations walked directly from the
chain, independent of any feed. If a graduation happened, it is in the
denominator whether or not anyone's API mentioned it.

## Why speed here is not the same as speed elsewhere

Detection is the cheap half. Knowing a token exists is worth very little on its
own; the pool address a migration hands you is not always the pool, and a
market cap you cannot compute is a call you cannot make.

That is the job of the next two layers.
