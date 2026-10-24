"""Command-line entry point."""

import logging
from typing import Annotated

import typer
from pydantic import ValidationError

from jobmath import __version__
from jobmath.logging_setup import configure_logging
from jobmath.settings import get_settings

logger = logging.getLogger(__name__)

app = typer.Typer(
    help="Rank job postings by fit with your résumé and explain each score.",
    no_args_is_help=True,
    add_completion=False,
)


@app.callback()
def main(
    verbose: Annotated[bool, typer.Option("--verbose", "-v", help="Enable debug logging.")] = False,
) -> None:
    try:
        settings = get_settings()
    except ValidationError as exc:
        typer.secho(f"Invalid environment settings:\n{exc}", fg="red", err=True)
        raise typer.Exit(code=2) from exc

    configure_logging("DEBUG" if verbose else settings.log_level)
    logger.debug("Settings loaded: %s", settings)


@app.command()
def version() -> None:
    """Show the installed version."""
    typer.echo(__version__)
