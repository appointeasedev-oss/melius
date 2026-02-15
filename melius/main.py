import click
import sys
import os
from rich.console import Console
from rich.table import Table
from .ollama_manager import OllamaManager
from .engine import AgentEngine

console = Console()
ollama = OllamaManager()

@click.group()
def cli():
    """Melius: A headless, local-first AI agent CLI."""
    pass

@cli.command()
@click.option("--model", default="llama3", help="Ollama model to use")
def start(model):
    """Start the Melius agent in interactive mode."""
    console.print(f"[bold green]Melius Agent Starting with model: {model}[/bold green]")
    
    # Check Ollama status
    ok, msg = ollama.check_ollama()
    if not ok:
        console.print(f"[bold red]Error:[/bold red] {msg}")
        return

    engine = AgentEngine(model=model)
    console.print("Type your instructions or 'exit' to quit.")
    
    while True:
        try:
            user_input = click.prompt("Melius > ")
            if user_input.lower() in ["exit", "quit"]:
                break
            
            with console.status("[bold blue]Thinking..."):
                response = engine.process_query(user_input)
            
            console.print(f"\n[bold green]Melius:[/bold green]\n{response}\n")
        except KeyboardInterrupt:
            break

@cli.command()
def list_models():
    """List available Ollama models."""
    models = ollama.list_models()
    if not models:
        console.print("[yellow]No models found or Ollama not running.[/yellow]")
        return
    
    table = Table(title="Available Ollama Models")
    table.add_column("Model Name", style="cyan")
    for m in models:
        table.add_row(m)
    console.print(table)

@cli.command()
@click.argument("model")
def download(model):
    """Download a model from Ollama."""
    console.print(f"[blue]Downloading {model}...[/blue]")
    if ollama.pull_model(model):
        console.print(f"[green]Successfully downloaded {model}[/green]")
    else:
        console.print(f"[red]Failed to download {model}[/red]")

@cli.command()
def setup():
    """Initial setup for Melius."""
    console.print("[bold blue]Setting up Melius...[/bold blue]")
    # Create necessary folders
    folders = ["workspace", "memory", "agents", "models", "tools"]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        console.print(f"Created folder: {folder}")
    
    ok, msg = ollama.check_ollama()
    if not ok:
        console.print(f"[yellow]Note: {msg}[/yellow]")
        console.print("Please install Ollama from https://ollama.com to use Melius.")
    else:
        console.print("[green]Ollama is ready![/green]")

if __name__ == "__main__":
    cli()
