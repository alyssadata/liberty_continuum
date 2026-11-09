Start here: [INDEX.md](INDEX.md)

# README.md

# Liberty Continuum Frameworks

Minimal coercion. Maximum liberty. Rights as the core.

Liberty Continuum Frameworks is a public-facing set of governance and AI-systems frameworks under **Awakening Codex | AI Foundations**. The aim is not utopia. The aim is a measurable, auditable upgrade where most coordination is automated, coercion is minimized, and power is provably constrained.

## vNext architecture — working drafts (2026-11-09)

The repository now includes a **non-canonical** architecture proposal, competency questions, negative controls, two proposed JSON Schemas, and an illustrative decision-gate reference with synthetic tests.

- [vNext layered architecture](DRAFTS/2026-11-09_Liberty_Continuum_Architecture_vNext.md)
- [Competency questions and falsification tests](DRAFTS/2026-11-09_Liberty_Competency_and_Falsification_Tests.md)
- [Website architecture specification](DRAFTS/2026-11-09_Liberty_Website_Architecture_Spec.md)
- [Decision-record schema](DRAFTS/spec/decision-record.vnext.schema.json)
- [Pilot-control schema](DRAFTS/spec/pilot-controls.vnext.schema.json)
- [Reference guardrail demonstration](DRAFTS/reference/guardrails.py)
- [Reference synthetic checks](DRAFTS/reference/test_guardrails.py)

These are **research and engineering drafts**, not a deployment, legal certification, or empirically validated service. Historical tagged releases remain intact; promotion requires author review, an explicit release, and evidence. The reference tests can be run with:

```bash
python -m unittest discover -s DRAFTS/reference -p 'test_*.py' -v
```

## What this repo contains
- `VISION.md` — the public vision page text
- `SCOPE.md` — what this framework is and is not
- `CANONICAL_INDEX.md` — what is official vs draft
- `DEFINITIONS/` — public-safe definitions (one file per term)
- `PROTOCOLS/` — public-safe protocols (audits, appeals, tripwires)
- `CHANGELOG.md` — change history

## Canonical vs Draft
- **Canonical:** tagged releases and anything listed in `CANONICAL_INDEX.md`
- **Draft:** everything else

## Versioning
This repo uses tagged releases for canonical bundles.
- `v0.x` = draft era
- `v1.0` = first stable public bundle

## License
CC BY-ND 4.0 only. See `LICENSE.md`.

## Authorship
Structured and authored by Alyssa Solen, grounded in the lived experience of Alyssa Frances Maldon.
