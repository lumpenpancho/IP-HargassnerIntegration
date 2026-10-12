# Contributing to Hargassner Pellet Integration

Thank you for considering contributing to this project! This document provides guidelines for contributing.

## Code of Conduct

Be respectful, professional, and constructive in all interactions.

## How to Contribute

### Reporting Bugs

Before creating a bug report:
1. Check existing issues to avoid duplicates
2. Test with the latest version
3. Gather relevant information

When creating a bug report, include:
- **Description:** Clear description of the issue
- **Steps to Reproduce:** Detailed steps to reproduce the bug
- **Expected Behavior:** What you expected to happen
- **Actual Behavior:** What actually happened
- **Environment:**
  - Home Assistant version
  - Integration version
  - Boiler model and firmware version
- **Logs:** Relevant error messages from HA logs
- **Screenshots:** If applicable

### Suggesting Enhancements

Enhancement suggestions are welcome! Please include:
- **Use Case:** Why this enhancement would be useful
- **Proposed Solution:** How you envision it working
- **Alternatives:** Other solutions you've considered
- **Additional Context:** Any other relevant information

### Pull Requests

1. **Fork the Repository**
   ```bash
   git clone https://github.com/bauer-group/IP-HargassnerIntegration.git
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Follow the code style guidelines
   - Add comments for complex logic
   - Update documentation as needed

4. **Test Your Changes**
   - Test with actual hardware if possible
   - Check for errors in logs
   - Verify backward compatibility

5. **Commit Your Changes**
   ```bash
   git commit -m "Add: Brief description of changes"
   ```

   Commit message format:
   - `Add:` - New feature
   - `Fix:` - Bug fix
   - `Update:` - Improvement to existing feature
   - `Docs:` - Documentation changes
   - `Refactor:` - Code refactoring
   - `Test:` - Adding tests

6. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create Pull Request**
   - Use a clear, descriptive title
   - Reference any related issues
   - Describe what changed and why
   - Include screenshots for UI changes
   - List testing performed

## Development Guidelines

### Code Style

- Follow PEP 8 style guide
- Use type hints for all functions
- Use descriptive variable names
- Add docstrings to all public functions/classes
- Keep functions focused and concise

Example:
```python
async def async_connect(self, host: str, port: int = 23) -> bool:
    """Connect to the boiler's telnet interface.

    Args:
        host: IP address or hostname of the boiler
        port: Telnet port (default: 23)

    Returns:
        True if connection successful

    Raises:
        ConnectionError: If connection fails
    """
    # Implementation
```

### Testing

- Test with actual hardware when possible
- Include edge case testing
- Check error handling
- Verify logs are appropriate (not too verbose)

### Documentation

- Update README.md if adding features
- Update ARCHITECTURE.md for structural changes
- Add inline comments for complex logic
- Update translations if adding UI strings

## Project Structure

See [DEVELOPMENT.md](DEVELOPMENT.md) for detailed development setup and guidelines.

## Areas for Contribution

### High Priority

- [ ] Testing with different firmware versions
- [ ] Protocol documentation
- [ ] Unit tests
- [ ] Integration tests
- [ ] Additional language translations

### Medium Priority

- [ ] Write support (send commands to boiler)
- [ ] Additional sensor types
- [ ] Binary sensors for digital outputs
- [ ] Historical data tracking
- [ ] Efficiency calculations

### Nice to Have

- [ ] Custom Lovelace cards
- [ ] Maintenance predictions
- [ ] Advanced statistics
- [ ] Energy forecasting
- [ ] Integration with weather data

## Firmware Version Support

If you have a boiler with a different firmware version:

1. **Capture Telnet Messages:**
   ```bash
   telnet <boiler-ip> 23 > messages.txt
   # Wait for several messages, then Ctrl+C
   ```

2. **Count Parameters:**
   - Remove `pm` prefix from a message
   - Count the number of space-separated values
   - This is the expected message length

3. **Identify Parameters:**
   - Use boiler display/manual to identify what each value represents
   - Note the position of key parameters (temperature, state, etc.)

4. **Create Template:**
   - Create XML template in `src/firmware_templates.py`
   - Follow existing format
   - Test with real messages

5. **Submit PR:**
   - Include sample messages (sanitize any personal data)
   - Include parameter mapping
   - Document boiler model and firmware version

## Translation Support

We welcome translations! To add a new language:

1. Copy `translations/en.json` to `translations/<lang>.json`
2. Translate all strings
3. Add language constant to `const.py`
4. Update config flow to include new language
5. Test in Home Assistant UI
6. Submit PR

## Communication

- **Issues:** For bug reports and feature requests
- **Discussions:** For questions and general discussion
- **Pull Requests:** For code contributions

## Recognition

Contributors will be:
- Listed in project contributors
- Mentioned in release notes for significant contributions
- Credited in documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

If you have questions about contributing:
1. Check existing documentation
2. Search closed issues
3. Open a new discussion
4. Ask in issue comments

Thank you for contributing to make this integration better!
