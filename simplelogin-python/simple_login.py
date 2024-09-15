from typing import Annotated
import typer
import utils.connector as connector
import settings
import warnings
from services.aliases_service import AliasesService
from utils.environment import get_token, save_token
from utils.output import pretty_print_aliases, print_alias, print_aliases

app = typer.Typer()

if settings.VERIFY_SSL == False:
    warnings.filterwarnings('ignore')

@app.command()
def set_token(token: Annotated[
        str,
        typer.Argument(
            help="The token created in the SimpleLogin dashboard",
        )]):

    save_token(token)
    print("Token saved!")

@app.command()
def list(verbose: Annotated[
        bool,
        typer.Option(
            help="Display aliases properties in a table",
        )] = False):
    print(f"Listing all aliases")
    service = AliasesService(get_token())
    if verbose:
        pretty_print_aliases(service.aliases)
    else:
        print_aliases(service.aliases)

@app.command()
def create():
    print(f"Creating a new random alias")
    service = AliasesService(get_token())
    alias = service.new_random_alias()
    print_alias(alias)

@app.command()
def delete(id: Annotated[
        int,
        typer.Argument(
            help="The id of the alias to delete",
        )]):
    print(f"Deleting alias #{id}")
    service = AliasesService(get_token())
    alias = service.get_alias(id)
    if alias == None:
        print(f"Alias #{id} not found")
        return
    
    if alias.pinned:
        print(f"{alias.email} is pinned and cannot be deleted")
        return
    
    confirm = typer.prompt(f"Do you really want to delete {alias.email} ? (y/n)")

    if confirm.lower() == "y":
        service.remove_alias(id)
        print(f"{alias.email} deleted!")

if __name__ == "__main__":
    app()