import click
import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from .ollama_manager import OllamaManager
from .agent import Orchestrator
from .config import Config

console = Console()
ollama = OllamaManager()

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """Melius: The Ultimate Headless Local AI Agent.
    
    If no command is provided, starts the interactive session.
    """
    if ctx.invoked_subcommand is None:
        ctx.invoke(start)

@cli.command()
@click.option("--model", default=Config.DEFAULT_MODEL, help="Ollama model to use")
def start(model):
    """Start the Melius Orchestrator in interactive mode."""
    console.print(Panel.fit("[bold cyan]Melius Prime Online[/bold cyan]\n[dim]Local. Headless. Self-Improving.[/dim]", border_style="blue"))
    
    # Check Ollama
    ok, msg = ollama.check_ollama()
    if not ok:
        console.print(f"[bold red]Error:[/bold red] {msg}")
        console.print("[yellow]Tip: Run 'melius setup' to check requirements.[/yellow]")
        return

    orchestrator = Orchestrator(model=model)
    console.print(f"[green]Using model:[/green] {model}")
    console.print("[dim]Type 'exit' to quit, 'help' for agent capabilities.[/dim]\n")
    
    while True:
        try:
            user_input = click.prompt("Melius > ")
            if user_input.lower() in ["exit", "quit"]:
                break
            
            with console.status("[bold blue]Processing..."):
                response = orchestrator.handle_task(user_input)
            
            console.print(f"\n[bold cyan]Melius:[/bold cyan]\n{response}\n")
        except KeyboardInterrupt:
            break

@cli.command()
def list_tools():
    """List all currently registered tools and skills."""
    from .tools import ToolRegistry
    registry = ToolRegistry()
    table = Table(title="Melius Tool Registry")
    table.add_column("Tool Name", style="cyan")
    table.add_column("Description", style="white")
    
    for tool in registry.tools.values():
        table.add_row(tool.name, tool.description)
    
    console.print(table)

@cli.command()
def setup():
    """Run production-ready setup and environment check."""
    console.print("[bold blue]Running Melius Environment Check...[/bold blue]")
    Config.ensure_dirs()
    
    # Check Ollama
    ok, msg = ollama.check_ollama()
    status = "[green]OK[/green]" if ok else "[red]FAILED[/red]"
    console.print(f"Ollama Status: {status} - {msg}")
    
    # Check GH CLI
    gh_check = os.system("gh --version > nul 2>&1")
    gh_status = "[green]OK[/green]" if gh_check == 0 else "[yellow]NOT FOUND[/yellow]"
    console.print(f"GitHub CLI: {gh_status}")
    
    console.print("\n[bold green]Setup complete![/bold green] You can now run 'melius start'.")

@cli.command()
@click.argument("model_name")
def download(model_name):
    """Download a specific model via Ollama."""
    console.print(f"Pulling model: {model_name}...")
    if ollama.pull_model(model_name):
        console.print(f"[green]Successfully downloaded {model_name}[/green]")
    else:
        console.print(f"[red]Failed to download {model_name}[/red]")

if __name__ == "__main__":
    cli()
