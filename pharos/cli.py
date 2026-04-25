import typer
from rich.console import Console
from rich.table import Table

from pharos.banner import print_banner
from pharos.exporters import export_csv, export_json
from pharos.scanner import scan_network

app = typer.Typer(
    help="Pharos - Local network visibility from the command line.",
    no_args_is_help=True,
)
console = Console()


@app.callback()
def main() -> None:
    """Pharos CLI entry point."""


@app.command()
def scan(
    range: str = typer.Option(..., "--range", "-r", help="CIDR range to scan, e.g. 192.168.1.0/24"),
    timeout: int = typer.Option(2, "--timeout", "-t", help="ARP response timeout"),
    json_out: str = typer.Option(None, "--json", help="Export results to JSON file"),
    csv_out: str = typer.Option(None, "--csv", help="Export results to CSV file"),
):
    print_banner()
    console.print(f"[bold green][+] Scanning range:[/bold green] {range}")

    results = scan_network(range, timeout)

    if not results:
        console.print("[yellow][-] No assets discovered.[/yellow]")
        raise typer.Exit()

    table = Table(title="Discovered Assets")
    table.add_column("IP Address", style="cyan")
    table.add_column("MAC Address", style="magenta")
    table.add_column("Vendor", style="white")
    table.add_column("Type", style="green")
    table.add_column("Risk Hint", style="yellow")

    for item in results:
        table.add_row(
            item["ip"],
            item["mac"],
            item["vendor"],
            item["asset_type"],
            item["risk_hint"],
        )

    console.print(table)

    if json_out:
        export_json(results, json_out)
        console.print(f"[green][+] JSON exported to:[/green] {json_out}")

    if csv_out:
        export_csv(results, csv_out)
        console.print(f"[green][+] CSV exported to:[/green] {csv_out}")


if __name__ == "__main__":
    app()
