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

## The product

### The bot — [@EyezOnBot](https://t.me/EyezOnBot)

Where the calls land, and where you do the work. Paste any contract address and
it scans it — no command needed.

| | |
|---|---|
| `/latest` · `/calls` | the record — every call, winners and losers |
| `/p` · `/chart` | price, chart and scan for any token |
| `/security` | rug and safety check |
| `/whales` | whale intel on a token |
| `/track` · `/tokens` | track a token, then see what you're watching |
| `/alerts` · `/setdefault` · `/heatalerts` | price alerts on, off or your own %, and crowd-heat straight to your DMs |
| `/wallet` · `/wallets` | wallet watch and P&L |
| `/tellme` | the narrative on any coin |
| `/topten` · `/bigbrains` | top holders, and which wallets are smart money |
| `/radar` | claim your profile on the site |
| `/coach` · `/journal` | a mentor on your own trading history |
| `/account` · `/referrals` · `/pro` | your status, invites, upgrade |

Win cards fire automatically when a call peaks.

### The site — [eyezon.gg](https://eyezon.gg)

**[Perception](https://eyezon.gg/perception)** — the hub. Where the engine's
work lives.

**[Radar](https://eyezon.gg/radar)** — crowd attention, the Hall of Fame, and
the Eye Watch strip. Who is looking, and how hard.

**[Aura](https://eyezon.gg/aura)** — the high-aura board. What the crowd is
turning toward before it's obvious.

**[The record](https://eyezon.gg/perception-signals)** — every call we have
published, in public.

**[IRIS](https://eyezon.gg/iris)** — the data engine, in the open.

**[Profile](https://eyezon.gg/profile)** — your home base. Watchlists, friends,
your own assistant.

**[Coach](https://eyezon.gg/coach)** — a mentor that reads your actual history,
not generic advice.

**[Social](https://eyezon.gg/social)** — friends and DMs, anon-first.

**[The 48h board](https://eyezon.gg/app)** — installable, everything live from
the last two days.

Every call also gets a share card — one link, the whole call, readable by
anyone.

### Free and Pro

Free gets you the past. Pro gets you the present.

| | Free | Pro |
|---|---|---|
| Scan any token, security, the public record | ✓ | ✓ |
| Track | 10 tokens | 250, custom ±% |
| Wallets | 1 | 5 |
| Whale intel | count | names, tier, P&L, win-rate |
| Call history | latest 10 | the full book |
| Crowd-heat | on the board | straight to your DMs |
| Ask the AI | 5 a day | unlimited |
| The live channel | — | calls as they fire |
| Aura board · Radar | teaser | unblurred |

**0.1 SOL a week.** 0.3 monthly, 0.8 for three months, 1.3 for six, 2.3 for a
year. [Upgrade](https://eyezon.gg/checkout) or `/pro` in the bot.

Free community: [t.me/eyezonchat](https://t.me/eyezonchat)

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

## Creator fees

pump.fun can route a share of a coin's creator fees to a GitHub account. If
you've launched something that builds on this work and want to send fees back
to the project, point them at [**@Sudiyasa1**](https://github.com/Sudiyasa1) —
the account behind this repo.

It buys no endorsement, no listing and no call.

## Not financial advice

Memecoins are high-risk. Nothing here is a recommendation to buy anything.
Do your own research and trade your own size.
