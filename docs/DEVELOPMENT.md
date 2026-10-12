# Development Guide

## Development Setup

### Prerequisites

- Python 3.11 or later
- Home Assistant development environment
- Git

### Local Development Environment

1. **Clone Home Assistant Core:**
```bash
git clone https://github.com/home-assistant/core.git
cd core
```

2. **Create Virtual Environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. **Install Dependencies:**
```bash
pip install -r requirements_dev.txt
pip install -r requirements_test.txt
```

4. **Link Custom Component:**
```bash
# Create custom_components directory
mkdir -p config/custom_components

# Symlink this integration
ln -s /path/to/BAUERGROUP.Internal.Integration.Hargassner/custom_components/bauergroup_hargassnerintegration config/custom_components/bauergroup_hargassnerintegration
```

### Running Home Assistant Development Server

```bash
hass -c config
```

Access at http://localhost:8123

## Code Style

### Formatting

Use `black` for code formatting:
```bash
black custom_components/bauergroup_hargassnerintegration/
```

### Linting

Use `pylint`:
```bash
pylint custom_components/bauergroup_hargassnerintegration/
```

Use `mypy` for type checking:
```bash
mypy custom_components/bauergroup_hargassnerintegration/
```

### Import Order

Follow Home Assistant conventions:
1. Python standard library
2. Third-party libraries
3. Home Assistant core
4. Local imports

Example:
```python
from __future__ import annotations

import asyncio
import logging
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity

from .const import DOMAIN
```

## Project Structure

```
BAUERGROUP.Internal.Integration.Hargassner/
├── custom_components/bauergroup_hargassnerintegration/
│   ├── __init__.py              # Integration setup
│   ├── config_flow.py          # Configuration UI
│   ├── const.py                # Constants
│   ├── coordinator.py          # Data coordinator
│   ├── exceptions.py           # Custom exceptions
│   ├── types.py                # Type definitions
│   ├── firmware_templates.py   # Firmware templates
│   ├── message_parser.py       # Message parser
│   ├── telnet_client.py        # Telnet client
│   ├── sensor.py               # Sensor platform
│   ├── manifest.json           # Metadata
│   ├── icon.png                # Integration icon
│   └── translations/           # Localization
│       ├── en.json
│       └── de.json
├── docs/                       # Documentation
│   ├── ARCHITECTURE.md
│   ├── DEVELOPMENT.md
│   ├── INSTALLATION.md
│   ├── CONTRIBUTING.md
│   ├── ADDING_FIRMWARE.md
│   └── ADDING_FIRMWARE_DE.md
├── tools/                      # Development tools
│   ├── daq_parser.py
│   ├── message_generator.py
│   ├── parameter_validator.py
│   └── telnet_tester.py
├── tests/                      # Tests
│   └── test_message_parser.py
├── firmware/                   # Firmware DAQ files
├── benchmarks/                 # Performance benchmarks
├── README.md
├── LICENSE
└── release.py                  # Release automation
```

## Testing

### Manual Testing

1. **Connection Test:**
```python
# In Home Assistant Python shell
from custom_components.bauergroup_hargassnerintegration.telnet_client import HargassnerTelnetClient

client = HargassnerTelnetClient(host="192.168.1.100", firmware_version="V14_1HAR_q1")
await client.async_start()
await asyncio.sleep(5)
data = await client.get_latest_data()
print(data)
await client.async_stop()
```

2. **Message Parsing Test:**
```python
from custom_components.bauergroup_hargassnerintegration.message_parser import HargassnerMessageParser

parser = HargassnerMessageParser("V14_1HAR_q1")
message = "pm 7 10.1 9.0 67.4 70 64.5 65 11 91.3 ..."
result = parser.parse_message(message)
print(result)
```

### Unit Tests (Future)

Create tests in `tests/` directory:

```python
# tests/test_message_parser.py
import pytest
from custom_components.bauergroup_hargassnerintegration.message_parser import HargassnerMessageParser

def test_parse_valid_message():
    parser = HargassnerMessageParser("V14_1HAR_q1")
    message = "pm 7 10.1 9.0 67.4 ..."
    result = parser.parse_message(message)

    assert result is not None
    assert "TK" in result
    assert result["TK"]["value"] == 67.4
```

Run tests:
```bash
pytest tests/
```

## Debugging

### Enable Debug Logging

Add to `configuration.yaml`:
```yaml
logger:
  default: info
  logs:
    custom_components.bauergroup_hargassnerintegration: debug
```

### Common Issues

1. **Connection Timeouts:**
   - Check firewall settings
   - Verify telnet port 23 is open
   - Test with `telnet <ip> 23` manually

2. **Parsing Errors:**
   - Enable debug logging
   - Check message format matches template
   - Verify firmware version selection

3. **Encoding Issues:**
   - Look for replacement characters (�)
   - Check boiler's actual encoding
   - Add encoding to supported list

## Adding Features

### Adding a New Sensor

1. Define in `sensor.py`:
```python
STANDARD_SENSORS.append((
    "NewParam",  # Parameter key
    "New Sensor",  # Display name
    SensorDeviceClass.TEMPERATURE,  # Device class
    SensorStateClass.MEASUREMENT,  # State class
    "mdi:icon",  # Icon
))
```

2. Test with actual boiler data

### Adding a New Firmware Version

1. Get XML template from boiler (if available) or reverse-engineer from messages

2. Add to `src/firmware_templates.py`:
```python
FIRMWARE_TEMPLATES["NANO_V15X"] = """<DAQPRJ>...</DAQPRJ>"""
```

3. Add to `const.py`:
```python
FIRMWARE_VERSIONS.append("NANO_V15X")
```

4. Test message parsing:
```python
parser = HargassnerMessageParser("NANO_V15X")
# Test with real messages
```

### Adding Translation

1. Create/edit translation files:
```json
// translations/fr.json
{
  "config": {
    "step": {
      "user": {
        "title": "Chaudière à Granulés Hargassner",
        ...
      }
    }
  }
}
```

2. Add language to `const.py`:
```python
LANGUAGE_FR = "FR"
```

## Contribution Workflow

### 1. Fork and Clone

```bash
git clone https://github.com/bauer-group/IP-HargassnerIntegration.git
cd IP-HargassnerIntegration
```

### 2. Create Feature Branch

```bash
git checkout -b feature/my-new-feature
```

### 3. Make Changes

- Follow code style guidelines
- Add comments for complex logic
- Update documentation if needed

### 4. Test Changes

- Test with actual boiler
- Check for errors in logs
- Verify all sensors work

### 5. Commit

```bash
git add .
git commit -m "Add: Description of changes"
```

Commit message format:
- `Add:` - New feature
- `Fix:` - Bug fix
- `Update:` - Improvement to existing feature
- `Docs:` - Documentation changes

### 6. Push and Create PR

```bash
git push origin feature/my-new-feature
```

Create pull request on GitHub with:
- Description of changes
- Testing performed
- Screenshots if UI changes

## Release Process

### Version Numbering

Follow Semantic Versioning (semver.org):
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes

### Creating a Release

1. Update version in `manifest.json`:
```json
{
  "version": "2.1.0"
}
```

2. Update CHANGELOG (if exists)

3. Create git tag:
```bash
git tag -a v2.1.0 -m "Release v2.1.0"
git push origin v2.1.0
```

4. Create GitHub release with release notes

## Performance Profiling

### Memory Usage

```python
import tracemalloc

tracemalloc.start()
# Run integration
await client.async_start()
await asyncio.sleep(60)
# Check memory
current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 1024 / 1024:.2f} MB")
print(f"Peak: {peak / 1024 / 1024:.2f} MB")
tracemalloc.stop()
```

### CPU Profiling

```python
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()
# Run code to profile
profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(20)
```

## Home Assistant Integration Checklist

Before submitting to HA core (future):

- [ ] Config flow implemented
- [ ] Translations for all strings
- [ ] Device info provided
- [ ] Unique IDs for all entities
- [ ] No blocking I/O in event loop
- [ ] All async functions use `async_`
- [ ] Error handling for all network operations
- [ ] Tests with >95% coverage
- [ ] Documentation complete
- [ ] Code follows HA style guide
- [ ] No hard-coded strings (use constants)
- [ ] Integration quality score: Gold

## Resources

- [Home Assistant Developer Docs](https://developers.home-assistant.io/)
- [Integration Architecture](https://developers.home-assistant.io/docs/architecture_components)
- [Entity Guidelines](https://developers.home-assistant.io/docs/core/entity)
- [Config Flow](https://developers.home-assistant.io/docs/config_entries_config_flow_handler)
- [Python Asyncio](https://docs.python.org/3/library/asyncio.html)

## Getting Help

- Open an issue on GitHub
- Check existing issues for similar problems
- Join Home Assistant Discord
- Review architecture documentation

## Code Review Guidelines

When reviewing PRs:

1. **Functionality:**
   - Does it work as intended?
   - Are edge cases handled?
   - Is error handling adequate?

2. **Code Quality:**
   - Follows style guide?
   - Well-commented?
   - No code duplication?

3. **Performance:**
   - No blocking operations?
   - Efficient algorithms?
   - Memory-conscious?

4. **Testing:**
   - Has it been tested?
   - Test coverage sufficient?
   - Manual testing performed?

5. **Documentation:**
   - README updated?
   - Docstrings present?
   - Architecture docs updated?
