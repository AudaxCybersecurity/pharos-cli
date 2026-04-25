import csv
import json
from pathlib import Path


def export_json(results: list[dict], output_file: str) -> None:
    path = Path(output_file)
    with path.open("w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)


def export_csv(results: list[dict], output_file: str) -> None:
    path = Path(output_file)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["ip", "mac", "vendor", "asset_type", "risk_hint"]
        )
        writer.writeheader()
        writer.writerows(results)
