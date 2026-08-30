# THE LENS — scoring from our own tape

Price data has a failure mode that nobody advertises: when the market is
busiest, shared vendor endpoints rate-limit. Exactly when the most tokens are
graduating, the feed you depend on is most likely to stall.

If your pipeline waits on that feed, your coverage quietly collapses at the
worst possible moment — and it looks like nothing is happening rather than like
something is broken.

**The Lens is the answer to that.** It scores a token from *our own* swap tape —
the trades we have already read off the chain — instead of waiting for a vendor
to answer.

## What that changes

- A rate-limited vendor is an inconvenience, not a blind spot.
- Market cap and liquidity come from actual on-chain trades, not a cached
  quote of unknown age.
- The busiest hours, when opportunity is highest, are the hours we keep working.

## The discipline

The Lens never fabricates. If our own tape does not contain enough real trades
to size a token honestly, it returns **unknown** and the token waits — it does
not get zero-filled into a number that looks like data.

An unknown you can see beats a zero you believe.
