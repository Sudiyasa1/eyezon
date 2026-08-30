# EyezOn

**The machine that sees the aura first.**

Every pump.fun graduation, scanned in about a second. Priced from the chain in
seventeen. Scored, gated, and called before the timeline knows it exists.

**Live:** [eyezon.gg](https://eyezon.gg) · **Bot:** [@EyezOnBot](https://t.me/EyezOnBot)

---

## Built for the trenches

You already know the problem. Forty thousand tokens launch a day. By the time a
chart looks good on your feed, the entry is gone — and half of what does reach
you is somebody's bag, posted after they filled.

EyezOn is the other thing. No callers, no bags, no vibes. An engine that watches
every migration on Solana, prices it off the chain itself, and either calls it
or kills it — in the time it takes you to unlock your phone.

**46,400 tokens graduated since July 16. We called 3,117 of them.**

One in fifteen. The other fourteen failed something — liquidity too thin,
holders too stacked, buy pressure faked, or the contract carrying a rug
signature. Saying no is the product. Anyone can forward every launch.

## The record

Every call, timestamped the second it went out. Entry stamped. Peak tracked.
Nothing backfilled, nothing quietly deleted.

| | |
|---|---|
| **38.8%** | reached 2× |
| **11.3%** | reached 5× |
| **4.0%** | reached 10× |
| **2,021×** | best call — $CATE |
| **~63** | calls a day |
| **~17s** | graduation to priced, scored and decided |

Every one of the 3,117 is on the site right now, in order, with its number.
Go check them.

## The stack

**[IRIS](docs/iris.md)** — the detection layer. Holds a live websocket subscription to Solana and catches a
migration the moment it lands on chain, fastest observed inside **one second**.
Coverage is measured against chain truth, not against a vendor's word for it:
**100%** of graduations since 16 July.

**[THE LENS](docs/the-lens.md)** — our own scoring path. When a price vendor rate-limits or stalls,
The Lens scores the token off *our own* swap tape instead of waiting. No feed
sits between us and the chain when it matters.

**[PERCEPTION](docs/perception.md)** — the engine that decides. Liquidity depth, holder spread, buy
dominance, authenticity, rug-safety. It rejects most of what it sees and posts
what survives, with the entry stamped at that moment.

**[The ledger](docs/the-ledger.md)** — every call written down the second it goes out, then tracked to
its peak. Peaks are verified against traded prices afterwards, from one
canonical source, so two surfaces can never quietly tell you two different
numbers.

**Radar** — [eyezon.gg](https://eyezon.gg). The whole record, live, in public.

## How it works

**Detect.** A token completes its bonding curve and migrates to a PumpSwap
pool. A live websocket subscription puts it in front of us inside a second.

**Price.** We read the pool on-chain and derive a market cap from real swap
data — not a vendor feed that's already stale by the time it answers.

**Score.** Liquidity depth, holder spread, buy dominance, authenticity,
rug-safety. Most tokens fail here. That's the point.

**Call.** It posts with the entry market cap stamped at that exact moment, so
the number can never be flattered later.

**Track.** The peak is verified against traded prices afterwards, so a published
multiple is something you can check rather than something you're asked to
believe.

## In this repo

- [`mint-check/`](mint-check/) — the pre-ape safety check. Can the creator
  still print supply? Can they freeze your tokens? How much does the top ten
  hold? Public chain data, one command, no account needed.

- [`pool-validator/`](pool-validator/) — tell whether a Solana account is
  genuinely a PumpSwap AMM pool, or something else wearing the same shape.
  Point it at an address and it answers.

- [`brand/`](brand/) — the EyezOn and PERCEPTION marks.

The engine, the thresholds and the gates are ours and stay ours. What's here is
the part that's useful to you on its own.

## Not financial advice

Memecoins are high-risk. Nothing here is a recommendation to buy anything.
Do your own research and trade your own size.
