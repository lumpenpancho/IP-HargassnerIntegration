# Commit Message Guidelines

This project follows [Conventional Commits](https://www.conventionalcommits.org/) for semantic commit messages.

## Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Example:**
```
feat(parser): add support for NANO_V15X firmware

- Add XML template for NANO_V15X
- Update parser to handle new parameter count
- Add tests for new firmware version

Closes #42
```

## Commit Types

### 🎯 Primary Types (Most Common)

| Type | Description | Version Impact | Example |
|------|-------------|----------------|---------|
| `feat` | New feature | MINOR | `feat(sensors): add binary sensors for digital outputs` |
| `fix` | Bug fix | PATCH | `fix(telnet): resolve reconnection timeout issue` |
| `docs` | Documentation only | None | `docs(readme): update installation instructions` |
| `refactor` | Code refactoring (no feature/fix) | None/PATCH | `refactor(parser): simplify message extraction` |
| `perf` | Performance improvement | PATCH | `perf(telnet): optimize data buffering` |
| `test` | Adding/updating tests | None | `test(parser): add unit tests for edge cases` |

### 🔧 Secondary Types

| Type | Description | Version Impact | Example |
|------|-------------|----------------|---------|
| `build` | Build system changes | None/PATCH | `build(deps): update home assistant core to 2024.1` |
| `ci` | CI/CD changes | None | `ci: add GitHub Actions workflow` |
| `chore` | Maintenance tasks | None/PATCH | `chore: update .gitignore` |
| `style` | Code style (formatting) | None | `style: format with black` |
| `revert` | Revert previous commit | Depends | `revert: revert "feat: add write support"` |

### ⚠️ Breaking Changes

For breaking changes, add `!` after type and `BREAKING CHANGE:` in footer:

```
feat(config)!: change configuration schema

BREAKING CHANGE: Configuration schema changed to support new features.
Users must reconfigure the integration after update.

Migration guide:
1. Remove old integration
2. Add new integration via UI
3. Configure parameters
```

## Scopes (Optional)

Scopes specify which part of the codebase is affected:

| Scope | Description | Example |
|-------|-------------|---------|
| `telnet` | Telnet client | `fix(telnet): handle connection timeout` |
| `parser` | Message parser | `feat(parser): add NANO_V15X support` |
| `sensors` | Sensor platform | `feat(sensors): add power sensor` |
| `config` | Configuration/Config Flow | `fix(config): validate IP address format` |
| `coordinator` | Data coordinator | `perf(coordinator): reduce update interval` |
| `templates` | Firmware templates | `feat(templates): add complete parameter descriptions` |
| `translations` | Localization | `feat(translations): add French translation` |
| `docs` | Documentation | `docs(architecture): update telnet client section` |

## Subject Line

- **Use imperative mood**: "add" not "added" or "adds"
- **Don't capitalize first letter**: `add feature` not `Add feature`
- **No period at end**: `add feature` not `add feature.`
- **Maximum 72 characters**
- **Be specific but concise**

**Good:**
```
feat(parser): add support for NANO_V15X firmware
fix(telnet): resolve timeout on slow networks
docs(readme): update quick start guide
```

**Bad:**
```
Added new firmware support
Fixed bug
Update docs
```

## Body (Optional)

- Separate from subject with blank line
- Explain **what** and **why**, not **how**
- Wrap at 72 characters
- Use bullet points for multiple changes

**Example:**
```
feat(sensors): add energy dashboard support

- Create energy sensor with kWh calculation
- Add device class ENERGY
- Add state class TOTAL_INCREASING
- Update documentation for energy dashboard

This allows users to track pellet heating energy in the
Home Assistant Energy Dashboard.
```

## Footer (Optional)

Reference issues, pull requests, or breaking changes:

```
Closes #123
Fixes #456, #789
See also #111
BREAKING CHANGE: Configuration schema changed
```

## Examples by Type

### Feature Addition (MINOR)

```
feat(templates): add complete parameter descriptions

- Extract all 128 analog parameters from V14_1HAR_q1
- Add descriptions for heating circuits 1-6
- Add descriptions for cascade control
- Add descriptions for differential regulation

All parameters from DAQPRJ template now have human-readable
descriptions for better sensor naming.

Closes #15
```

### Bug Fix (PATCH)

```
fix(telnet): handle connection loss gracefully

- Add exponential backoff to reconnection logic
- Prevent reconnection loop on permanent failures
- Log connection attempts at debug level

Previously, connection losses would cause rapid reconnection
attempts. Now implements 5s → 10s → 20s → 300s backoff.

Fixes #28
```

### Documentation (No version change)

```
docs(installation): add troubleshooting section

- Add common connection issues
- Add encoding problem solutions
- Add debug logging instructions
```

### Refactoring (No version change or PATCH)

```
refactor(parser): simplify parameter extraction

- Remove duplicate code in parse_value()
- Extract bit manipulation to helper function
- Add type hints to internal methods

No functional changes, improved code maintainability.
```

### Breaking Change (MAJOR)

```
feat(config)!: migrate to config flow only

Remove YAML configuration support in favor of GUI-based
config flow for better user experience.

BREAKING CHANGE: YAML configuration no longer supported.

Migration steps:
1. Note your current configuration
2. Remove hargassner_pellet from configuration.yaml
3. Restart Home Assistant
4. Add integration via UI (Settings > Devices & Services)
5. Enter configuration from step 1

Closes #50
```

### Performance Improvement (PATCH)

```
perf(telnet): optimize message processing

- Process only latest message, discard older
- Reduce lock contention in data access
- Cache parsed parameter definitions

Reduces CPU usage by ~30% during high message rate.
```

## Commit Message Checklist

Before committing, verify:

- [ ] Type is correct (`feat`, `fix`, `docs`, etc.)
- [ ] Scope is appropriate (if used)
- [ ] Subject uses imperative mood
- [ ] Subject is lowercase and max 72 chars
- [ ] Subject has no period at end
- [ ] Body explains what and why (if needed)
- [ ] Footer references issues (if applicable)
- [ ] Breaking change noted in footer (if applicable)

## Tools

### Commitizen

Install commitizen for interactive commit messages:

```bash
npm install -g commitizen cz-conventional-changelog
```

Usage:
```bash
git add .
git cz
```

### Git Hooks

Add pre-commit hook to validate messages:

```bash
# .git/hooks/commit-msg
#!/bin/sh
commit_msg=$(cat "$1")

# Check format: type(scope): subject
if ! echo "$commit_msg" | grep -qE "^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(\(.+\))?: .{1,72}"; then
    echo "❌ Commit message does not follow Conventional Commits format"
    echo ""
    echo "Format: <type>(<scope>): <subject>"
    echo ""
    echo "Example: feat(parser): add NANO_V15X support"
    exit 1
fi

echo "✅ Commit message format valid"
```

## Multi-Line Commits

Use git commit without `-m` for multi-line messages:

```bash
git add .
git commit
# Opens editor for full commit message
```

In editor:
```
feat(sensors): add energy dashboard support

- Create energy sensor with kWh calculation
- Add device class ENERGY
- Add state class TOTAL_INCREASING

Allows tracking pellet heating energy in HA Energy Dashboard.

Closes #25
```

## Amending Commits

Fix last commit message:

```bash
git commit --amend
```

**Note:** Only amend commits that haven't been pushed!

## Quick Reference

**Most common patterns:**

```bash
# New feature
git commit -m "feat(scope): add new feature"

# Bug fix
git commit -m "fix(scope): resolve specific issue"

# Documentation
git commit -m "docs(scope): update documentation"

# Refactoring
git commit -m "refactor(scope): improve code structure"

# Performance
git commit -m "perf(scope): optimize performance"

# Breaking change
git commit -m "feat(scope)!: add breaking feature" -m "BREAKING CHANGE: details"
```

## Integration with Semantic Versioning

Commit types map to version bumps:

| Commit Type | Version Bump | Automation |
|-------------|--------------|------------|
| `feat` | MINOR (0.X.0) | Automated |
| `fix`, `perf` | PATCH (0.0.X) | Automated |
| `BREAKING CHANGE` | MAJOR (X.0.0) | Automated |
| Others | None | Manual decision |

## Enforcement

**Recommended:** Use Git hooks or CI/CD to enforce commit message format.

**GitHub Actions example:**
```yaml
name: Validate Commits
on: [pull_request]
jobs:
  commitlint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: wagoid/commitlint-github-action@v5
```

## References

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Angular Commit Guidelines](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit)
- [Commitizen](https://github.com/commitizen/cz-cli)
