# Pharos

**Local network visibility from the command line.**

Pharos is a lightweight CLI tool for authorized local network asset visibility, inventory enrichment, and reporting.

It helps teams quickly understand what devices are present on a local network, enrich observed assets with vendor information, classify common device categories, and export evidence-ready results.

## Positioning

Pharos is designed as a practical visibility layer for security teams, auditors, administrators, and lab environments.

It focuses on asset awareness, not exploitation.

Before hardening, validation, or resilience planning, teams need to answer a basic question:

> What actually exists inside the network?

Pharos helps provide that first layer of visibility.

## Features

- ARP-based local network discovery
- MAC vendor enrichment
- Improved asset classification
- IoT and smart-device detection hints
- Risk hints for common device categories
- Clean terminal table output
- JSON export
- CSV export
- Standalone HTML report generation
- Python packaging with a CLI entry point
- Basic automated tests

## Example Terminal Output

```text
PHAROS - Local Network Visibility CLI

[+] Scanning range: 192.168.1.0/24

Discovered Assets
IP Address      MAC Address          Vendor                               Type                    Risk Hint
192.168.1.1     74:24:9f:80:b5:d1    TIBRO Corp.                          Network Infrastructure  Management or critical network asset - validate admin exposure
192.168.1.181   58:05:d9:0f:09:4b    Seiko Epson Corporation              Printer / Office Device Often overlooked office asset - review admin interface and firmware
192.168.1.199   f0:c9:d1:32:ba:2c    GD Midea Air-Conditioning Equipment  Smart Home / IoT        IoT device - verify isolation, firmware posture, and business need
```

## Installation

Run the installation commands from the repository root, not from inside the `pharos/` package directory.

```bash
git clone https://github.com/AudaxCybersecurity/pharos-cli.git
cd pharos-cli
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

Export JSON and CSV:

```bash
sudo venv/bin/pharos --range 192.168.1.0/24 --json results.json --csv results.csv
```

Generate an HTML report:

```bash
sudo venv/bin/pharos --range 192.168.1.0/24 --html pharos-report.html
```

Generate all outputs:

```bash
sudo venv/bin/pharos --range 192.168.1.0/24 --json results.json --csv results.csv --html pharos-report.html
```

Use a custom timeout:

```bash
sudo venv/bin/pharos --range 192.168.1.0/24 --timeout 3
```

## Asset Classification

Pharos uses conservative vendor-based classification to provide quick inventory hints. Current categories include:

- Network Infrastructure
- Camera / Surveillance IoT
- Smart Home / IoT
- Printer / Office Device
- Endpoint / Mobile
- Workstation / Endpoint
- Virtualized Asset
- Embedded / Lab IoT
- Generic Network Asset
- Unknown Asset

## Project Structure

```text
pharos-cli/
├── pharos/
│   ├── __init__.py
│   ├── banner.py
│   ├── classifier.py
│   ├── cli.py
│   ├── exporters.py
│   ├── report.py
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

- Screenshots and visual examples
- Watch mode for newly observed devices
- Passive observation mode
- Subnet auto-detection
- Optional lightweight service enrichment
- Docker image
- Better asset classification rules
- HTML report templates

## Responsible Use

Pharos is intended for authorized internal visibility, asset inventory, lab use, and defensive assessment workflows.

Use it only in environments where you have permission.

## License

MIT License.
