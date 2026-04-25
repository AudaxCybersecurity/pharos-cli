# Pharos

Pharos is a lightweight command-line tool for local network asset visibility.

It helps authorized teams create a quick inventory of devices observed on a local network, enrich them with vendor information, classify common asset types, and export results for reporting.

## Purpose

Before security teams can improve resilience, they need a clear view of what exists inside their environment.

Pharos focuses on visibility, asset awareness, and reporting.

## Current Version

v0.1.0

## Features

- Local network asset discovery
- MAC vendor enrichment
- Basic asset classification
- Risk hints for common device categories
- JSON export
- CSV export
- Clean terminal output
- Python packaging with a CLI entry point
- Basic automated tests

## Project Structure

```text
pharos-cli/
├── pharos/
│   ├── __init__.py
│   ├── banner.py
│   ├── classifier.py
│   ├── cli.py
│   ├── exporters.py
│   └── scanner.py
├── examples/
│   └── sample-output.json
├── tests/
│   └── test_classifier.py
├── .github/workflows/python.yml
├── .gitignore
├── LICENSE
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Installation

Run the installation commands from the repository root, not from inside the `pharos/` package directory.

```bash
cd ~/pharos-cli
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -e .
```

Confirm the CLI is installed:

```bash
which pharos
pharos --help
```

## Usage

When using a virtual environment, `sudo pharos` may not find the command because sudo uses a different PATH. Use the executable inside the virtual environment:

```bash
cd ~/pharos-cli
source venv/bin/activate
sudo venv/bin/pharos --range 192.168.1.0/24
```

Export results:

```bash
sudo venv/bin/pharos --range 192.168.1.0/24 --json results.json --csv results.csv
```

Use a custom timeout:

```bash
sudo venv/bin/pharos --range 192.168.1.0/24 --timeout 3
```

## Example Output

```text
PHAROS - Local Network Visibility CLI

Discovered Assets
IP Address      MAC Address          Vendor             Type                    Risk Hint
192.168.1.1     aa:bb:cc:dd:ee:ff    MikroTik           Network Infrastructure  Management or critical network asset
192.168.1.45    11:22:33:44:55:66    Hikvision          Camera / IoT            Surveillance or unmanaged IoT asset
```

## Development

Install development dependencies:

```bash
cd ~/pharos-cli
source venv/bin/activate
pip install -e .[dev]
```

Run tests:

```bash
pytest
```

## Roadmap

- Watch mode for newly observed devices
- Passive observation mode
- HTML reporting
- Subnet auto-detection
- Optional lightweight service enrichment
- Docker image
- Better asset classification rules

## Responsible Use

Pharos is intended for authorized internal visibility, asset inventory, lab use, and defensive assessment workflows.

Use it only in environments where you have permission.

## License

MIT License.
