from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from html import escape
from pathlib import Path


def generate_html_report(results: list[dict], output_file: str, scan_range: str) -> None:
    """Generate a simple standalone HTML report for discovered assets."""

    path = Path(output_file)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    type_counts = Counter(item.get("asset_type", "Unknown") for item in results)

    rows = "\n".join(
        f"""
        <tr>
            <td>{escape(item.get('ip', ''))}</td>
            <td>{escape(item.get('mac', ''))}</td>
            <td>{escape(item.get('vendor', ''))}</td>
            <td>{escape(item.get('asset_type', ''))}</td>
            <td>{escape(item.get('risk_hint', ''))}</td>
        </tr>
        """
        for item in results
    )

    summary_cards = "\n".join(
        f"""
        <div class="card">
            <span class="metric">{count}</span>
            <span class="label">{escape(asset_type)}</span>
        </div>
        """
        for asset_type, count in sorted(type_counts.items())
    )

    html = f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Pharos Network Visibility Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 0; background: #0f172a; color: #e5e7eb; }}
        header {{ padding: 32px; background: #111827; border-bottom: 1px solid #374151; }}
        main {{ padding: 32px; }}
        h1 {{ margin: 0 0 8px 0; font-size: 32px; }}
        .subtitle {{ color: #9ca3af; }}
        .summary {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; margin: 24px 0; }}
        .card {{ background: #1f2937; border: 1px solid #374151; border-radius: 14px; padding: 18px; }}
        .metric {{ display: block; font-size: 30px; font-weight: 700; }}
        .label {{ display: block; color: #9ca3af; margin-top: 6px; }}
        table {{ width: 100%; border-collapse: collapse; background: #111827; border-radius: 14px; overflow: hidden; }}
        th, td {{ padding: 12px 14px; border-bottom: 1px solid #374151; text-align: left; vertical-align: top; }}
        th {{ background: #1f2937; color: #f9fafb; }}
        td {{ color: #d1d5db; }}
        footer {{ margin-top: 24px; color: #9ca3af; font-size: 13px; }}
    </style>
</head>
<body>
    <header>
        <h1>Pharos Network Visibility Report</h1>
        <div class="subtitle">Range: {escape(scan_range)} | Assets: {len(results)} | Generated: {generated_at}</div>
    </header>
    <main>
        <section class="summary">
            {summary_cards}
        </section>
        <section>
            <table>
                <thead>
                    <tr>
                        <th>IP Address</th>
                        <th>MAC Address</th>
                        <th>Vendor</th>
                        <th>Asset Type</th>
                        <th>Risk Hint</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
        </section>
        <footer>
            Pharos provides asset visibility hints for authorized internal assessment and inventory workflows.
        </footer>
    </main>
</body>
</html>
"""

    path.write_text(html, encoding="utf-8")
