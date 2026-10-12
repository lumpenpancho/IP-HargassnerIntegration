# Semantic Versioning Guide

This project follows [Semantic Versioning 2.0.0](https://semver.org/).

## Version Format

**MAJOR.MINOR.PATCH** (e.g., `2.1.3`)

- **MAJOR**: Incompatible API changes or breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

## Version Types

### MAJOR Version (X.0.0)

Increment MAJOR version when making incompatible or breaking changes:

**Examples:**
- Changing configuration schema (requires users to reconfigure)
- Removing sensors or entities
- Changing entity IDs or unique IDs
- Changing API/function signatures (for programmatic use)
- Dropping support for firmware versions
- Changing telnet protocol handling (breaking existing connections)

**Current:** `0.1.0` (Initial release candidate)

### MINOR Version (0.X.0)

Increment MINOR version when adding new features (backward compatible):

**Examples:**
- Adding new sensors or parameters
- Adding new firmware version support
- Adding new configuration options (with defaults)
- Adding new features (write support, diagnostics, etc.)
- Improving performance significantly
- Adding translations for new languages

**Example:**
- `0.2.0` - Add support for NANO_V15X firmware
- `0.3.0` - Add binary sensors for digital outputs
- `0.4.0` - Add write support (send commands to boiler)

### PATCH Version (0.0.X)

Increment PATCH version for bug fixes and minor improvements:

**Examples:**
- Fixing connection issues
- Fixing parsing errors
- Fixing encoding issues
- Improving error handling
- Updating documentation
- Fixing typos or UI text
- Performance improvements (minor)
- Dependency updates (security/bug fixes)

**Example:**
- `0.1.1` - Fix reconnection issue on network timeout
- `0.1.2` - Fix °C encoding for special characters
- `0.1.3` - Improve error logging

## Pre-release Versions

For development and testing:

**Format:** `X.Y.Z-alpha.N`, `X.Y.Z-beta.N`, `X.Y.Z-rc.N`

**Examples:**
- `0.2.0-alpha.1` - Alpha release (early testing)
- `0.2.0-beta.1` - Beta release (feature complete, testing)
- `0.2.0-rc.1` - Release candidate (final testing)

## Build Metadata

Optional build information:

**Format:** `X.Y.Z+buildN` or `X.Y.Z+YYYYMMDD`

**Examples:**
- `0.1.0+20251122` - Build from November 22, 2025
- `0.1.0+build.1` - Build number 1

## Version Workflow

### 1. Development

During development, work on `main` branch or feature branches.

### 2. Before Release

1. **Update version** in `manifest.json`:
   ```json
   {
     "version": "0.2.0"
   }
   ```

2. **Update CHANGELOG.md**:
   ```markdown
   ## [0.2.0] - 2025-12-XX
   ### Added
   - Support for NANO_V15X firmware
   - Additional parameter descriptions

   ### Fixed
   - Connection timeout handling

   ### Changed
   - Improved encoding detection
   ```

3. **Tag the release**:
   ```bash
   git tag -a v0.2.0 -m "feat: add NANO_V15X firmware support"
   git push origin v0.2.0
   ```

### 3. Release Notes

Include in GitHub release:
- **What's New** - New features (MINOR)
- **Bug Fixes** - Fixes (PATCH)
- **Breaking Changes** - Breaking changes (MAJOR)
- **Upgrade Instructions** - If needed

## Compatibility Matrix

| Version | Home Assistant | Python | Status |
|---------|---------------|--------|--------|
| 0.1.x   | ≥ 2024.1      | ≥ 3.11 | Current |

## Decision Tree

Use this flowchart to decide version increment:

```
Does it break existing functionality?
├─ YES → MAJOR version
└─ NO
   └─ Does it add new features?
      ├─ YES → MINOR version
      └─ NO
         └─ Is it a bug fix or improvement?
            ├─ YES → PATCH version
            └─ NO → No version change needed
```

## Examples by Change Type

### MAJOR (Breaking Changes)

```
0.9.5 → 1.0.0
```

**Changes:**
- Stable API release
- Production-ready declaration
- Breaking changes if any accumulated during 0.x development

### MINOR (New Features)

```
0.1.0 → 0.2.0
```

**Changes:**
- Added NANO_V15X firmware support
- Added 20 new parameter descriptions
- Added French translation
- Added diagnostic sensors

### PATCH (Bug Fixes)

```
0.1.0 → 0.1.1
```

**Changes:**
- Fixed reconnection timeout bug
- Fixed encoding issue with umlauts
- Improved error logging
- Updated documentation

## Version History (Summary)

- **v0.1.0** (2025-11-22) - Initial release candidate
  - Config Flow (GUI configuration)
  - Thread-safe telnet client
  - Auto-reconnect with exponential backoff
  - Multi-encoding support
  - 138 parameter descriptions
  - DAQ parser tool
  - Comprehensive documentation

## Deprecation Policy

When deprecating features:

1. **Announce** in MINOR version (e.g., v0.3.0)
2. **Mark deprecated** in code (warnings in logs)
3. **Remove** in next MAJOR version (e.g., v1.0.0)

**Minimum deprecation period:** 3 months or 2 MINOR versions

## Questions?

**Q: Do documentation changes require a version bump?**
A: No, documentation-only changes don't require a version bump.

**Q: Do dependency updates require a version bump?**
A: Yes, PATCH version (e.g., `0.1.0` → `0.1.1`)

**Q: What if I'm unsure?**
A: When in doubt, increment PATCH. It's safer than MINOR.

## References

- [Semantic Versioning 2.0.0](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [Conventional Commits](https://www.conventionalcommits.org/)
