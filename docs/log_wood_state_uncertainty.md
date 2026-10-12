# Log wood (HV) ZK states: what's confirmed and what isn't

The `ZK` (Zustand Kessel) state names in `boiler_profiles.py` for the log wood
profile are inferred from DAQ log analysis, not read off a boiler display or
confirmed by Hargassner. This table lists every value where that inference is
shaky, so it can be dropped into a PR and the community can fill the gaps.

Evidence is from ten `.DAQ` archive files sampled across ~5 years and three
firmware versions (V10.2d1, V10.2l3, V10.2HAR.n2) from one HV20 installation,
plus three days of live telnet capture from the same boiler.

| ZK | Current name (en/de) | Confidence | Evidence | Open question |
|----|----|----|----|----|
| 5 | *(none, shows as "ZK 5")* | none | Never observed in any sample. | What is it, and when does it occur? |
| 7 | Full firing / Vollbrand | low | O2 drops to 2.5-6.6 % (lower than during ZK 6), flue gas 199-238 °C. Cycles 6 → 7 → 8 → 6 → 7 → 8 → 9 within a single burn. | Is this really a distinct "peak output" phase, or just a measurement artifact of the O2 sensor during the same burn as 6? |
| 8 | Ember preservation / Gluterhaltung | low | Flue gas 127-233 °C, primary air 12-40 %, consistently bridges from 6/7 toward burn-out (9). | Does it only ever follow 6/7, or can it occur independently? |
| 9 | Burn-out / Ausbrand | medium | Present in every sample. Duration (number of consecutive samples) differs between the oldest firmware (V10.2d1) and the newer ones - not yet explained. | Is the difference a firmware behaviour change, or just batch-size/wood-load dependent? |
| 11 | Cool-down / Nachlauf | medium | Present in every sample, always follows 9. The original 3-day analysis described this as "exactly 360 min" - that does **not** hold up against the wider archive; duration varies. | What actually ends this state - a timer, a temperature threshold, or a demand signal? |
| 12 | *(none, shows as "ZK 12")* | very low | Seen exactly once (one sample) in one file, nested *inside* a full-burn run: `...6 → 12 → 6 → 9...`, co-occurring with fault 24 ("Rücklaufanhebung Temperatur nicht erreicht" / return-temperature boost not reached). | Is this a named state at all, or just a one-tick side effect of the return-temperature fault? |
| 14 | *(none, shows as "ZK 14")* | very low | Seen exactly once (one sample) in one file, between "door open" (13) and "ignition preparation" (3): `...13 → 14 → 3 → 2 → 3 → 4...`. | Same question as 12 - real state or a one-tick transition blip? |

Also unconfirmed, not state-related:
- **dummy1/dummy2 ordering** in the firmware channel template - not yet resolved; needs a live telnet capture around the moment the hot water tank reaches 59 °C while firing.
- All state names above (including the ones with "medium" confidence: 1, 2, 3, 4, 6, 9, 11, 13) are inferred from timing and sensor values, not confirmed against the boiler's own display text.

If anyone from the community has a Hargassner HV/Neo-HV service manual, firmware
documentation, or has simply watched these ZK numbers scroll past on their own
boiler's display, a correction here would be very welcome.
