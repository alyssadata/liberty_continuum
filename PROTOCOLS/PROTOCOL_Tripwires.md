# PROTOCOLS/PROTOCOL_Tripwires.md

# PROTOCOL — Tripwires

## Purpose
Prevent drift into unaccountable power by freezing autonomy when accountability degrades.

## Tripwires that trigger a freeze
A system must automatically reduce autonomy when any of the following occur:
- Audit failure rates exceed threshold
- Logging integrity is compromised
- Model or rule provenance is broken
- Appeal backlog exceeds time bounds
- Bias metrics exceed allowed bounds
- Unexplained decision variance increases

## Freeze behavior
When triggered:
- Autonomy reduces to recommendation-only
- Human review required for impactful decisions
- Incident is publicly logged
- Remediation required before autonomy returns

## Public principle
If accountability degrades, autonomy freezes.
