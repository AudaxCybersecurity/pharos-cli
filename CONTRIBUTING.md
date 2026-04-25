# Contributing to Pharos

Thank you for your interest in contributing to Pharos.

Pharos is a defensive local network visibility tool. Contributions should support authorized asset discovery, inventory quality, reporting, and defensive assessment workflows.

## Good Contribution Areas

- Better asset classification rules
- Safer output handling
- Improved report templates
- Documentation improvements
- Tests
- Packaging improvements
- Defensive workflow examples
- Usability improvements

## Contributions We Will Not Accept

To keep the project focused and safe, Pharos will not accept contributions that add:

- Exploitation modules
- Credential collection
- Payload delivery
- Persistence
- Evasion
- Unauthorized scanning workflows
- Phishing functionality
- C2 functionality
- Instructions for misuse

## Development Setup

```bash
git clone https://github.com/AudaxCybersecurity/pharos-cli.git
cd pharos-cli
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -e .[dev]
pytest
```

## Pull Request Guidelines

Before opening a pull request:

1. Keep the change focused.
2. Add or update tests where practical.
3. Update documentation if behavior changes.
4. Avoid committing real network data, client data, public IP addresses, internal hostnames, or sensitive MAC addresses.
5. Explain the defensive use case clearly.

## Code Style

Prefer simple, readable Python with explicit behavior and minimal dependencies.

## Responsible Use

By contributing, you agree that the project should remain focused on authorized defensive visibility and resilience workflows.
