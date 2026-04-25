# Screenshots

This folder is reserved for sanitized Pharos screenshots.

Recommended files:

- `pharos-terminal.png` - terminal output with sanitized network data
- `pharos-html-report.png` - HTML report screenshot with sanitized network data

## Screenshot Safety Checklist

Before committing screenshots, remove or mask:

- Client names
- Public IP addresses
- Internal hostnames
- Sensitive MAC addresses
- Usernames
- Wi-Fi names
- VPN names
- Physical addresses
- Any production-only identifiers

Use documentation-safe sample data whenever possible.

## README Usage

```markdown
![Pharos terminal output](docs/screenshots/pharos-terminal.png)
![Pharos HTML report](docs/screenshots/pharos-html-report.png)
```
