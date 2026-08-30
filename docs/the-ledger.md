# The ledger

Every call is written down the second it goes out, and then tracked.

- **Entry** — stamped at the moment of the call, never revised.
- **Peak** — tracked continuously, then verified against traded prices.
- **Outcome** — recorded, win or loss. Nothing is deleted afterwards.

## One number, one source

A published multiple is read through a single canonical accessor. That sounds
like an implementation detail; it is the difference between a track record you
can trust and one you cannot.

When the same quantity is computed independently in several places, those places
eventually disagree — and the version a visitor sees becomes an accident of
which page they opened. One source means every surface reports the same figure
or none of them do.

## Verified, not asserted

A peak read is authoritative only for the window it actually observed. A
verified value never silently replaces a higher price recorded after that
observation — otherwise a still-running token would display a peak *below* its
current price, which cannot happen in reality and should never happen on a
screen.

The whole record is public at [eyezon.gg](https://eyezon.gg).
