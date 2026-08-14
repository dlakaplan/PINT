# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project, at least loosely, adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

This file contains the unreleased changes to the codebase. See CHANGELOG.md for
the released changes.

## Unreleased
### Changed
### Added
- Plot whitened DM residuals in pintk.
- `ssb_to_psb_xyz_ECL` and `ssb_to_psb_xyz_ICRS` are now cached
- Can now use INPOP ephemeris
- ELL1H with H3+STIGMA: add opt-in ``ell1h_shapiro="absorbed"`` to select Freire & Wex Eq. (28) (Tempo2 ELL1H/T2 mode 1). Default remains Eq. (29) ``"full"`` (`get_model` / `get_model_and_toas` / `ModelBuilder`).
### Fixed
- Jodrell Bank Mark II sites (``jbmk2`` / ``jbmk2roach`` / ``jbmk2dfb``) now follow TEMPO2's clock routing (equivalent to ``jbafb`` / ``jbroach`` / ``jbdfb``) instead of the default empty TEMPO clock path.
### Removed
