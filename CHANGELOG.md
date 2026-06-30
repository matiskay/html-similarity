# Changelog

All notable changes to this project are documented in this file.

## [0.4.0] - 2026-06-30

### Added
- Support loading HTML from `bytes` (not just `str`) in `structural_similarity` ([#111](https://github.com/matiskay/html-similarity/pull/111)).
- Type hints across the `html_similarity` package ([#110](https://github.com/matiskay/html-similarity/pull/110)).
- `HtmlParsingError` exception, raised by `structural_similarity` when a document genuinely fails to parse ([#117](https://github.com/matiskay/html-similarity/pull/117)).

### Fixed
- `get_tags` no longer raises on `HtmlProcessingInstruction` nodes (e.g. `<?php ... ?>`) — they're now tagged as `processing-instruction` ([#114](https://github.com/matiskay/html-similarity/pull/114)).
- `structural_similarity` no longer relies on `lxml` as an undeclared transitive dependency of `parsel`; `lxml` is now an explicit dependency ([#115](https://github.com/matiskay/html-similarity/pull/115)).
- `structural_similarity` no longer uses `difflib`'s default `autojunk=True`, which silently distorted similarity scores on large, repetitive HTML documents (≥200 tags dominated by repeated elements like `div`/`li`/`span`) ([#116](https://github.com/matiskay/html-similarity/pull/116)).

### Changed
- **Breaking:** `structural_similarity` now raises `HtmlParsingError` on a genuine parse failure instead of silently catching any exception, printing it, and returning `0.0` ([#117](https://github.com/matiskay/html-similarity/pull/117)).
- Minimum supported Python version raised to 3.14 ([#108](https://github.com/matiskay/html-similarity/pull/108)).
- CI migrated from Travis CI to GitHub Actions ([#109](https://github.com/matiskay/html-similarity/pull/109)).
- Added Dependabot configuration for `uv` and GitHub Actions ([#112](https://github.com/matiskay/html-similarity/pull/112)).

[0.4.0]: https://github.com/matiskay/html-similarity/releases/tag/v0.4.0
