import json
from typing import List
from rich.console import Console
from rich.table import Table
from .engine import PhantomFinding

console = Console()

class PhantomReporter:
    @staticmethod
    def print_terminal_report(findings: List[PhantomFinding]):
        if not findings:
            console.print("[green]? No parameter anomalies or mass-assignment vulnerabilities detected.[/green]")
            return

        table = Table(title="[bold red]ParamPhantom Mass-Assignment & Parameter Findings[/bold red]")
        table.add_column("Parameter", style="cyan", no_wrap=True)
        table.add_column("Injected Value", style="yellow")
        table.add_column("Status", style="magenta")
        table.add_column("Length Delta", style="green")
        table.add_column("Description", style="white")

        for f in findings:
            delta = f.injected_len - f.baseline_len
            table.add_row(
                f.parameter,
                f.payload_value,
                f"{f.baseline_status} -> {f.injected_status}",
                f"{delta:+d} bytes",
                f.description
            )
        console.print(table)

    @staticmethod
    def save_json_report(findings: List[PhantomFinding], filepath: str):
        data = [f.model_dump() for f in findings]
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        console.print(f"[bold green]? JSON report saved to {filepath}[/bold green]")
