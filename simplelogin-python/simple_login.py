import typer
import utils.connector as connector
import settings
import warnings
from services.aliases_service import AliasesService

app = typer.Typer()

if settings.VERIFY_SSL == False:
    warnings.filterwarnings('ignore')

@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def rawlist():
    print(f"Listing all aliases")
    #print(settings.TOKEN) 
    list = connector.get_aliases_from_sl(settings.TOKEN, 0)
    print(list)


@app.command()
def list(all: bool = False):
    print(f"Listing all aliases")
    service = AliasesService(settings.TOKEN)
    if all:
        service.pretty_print_aliases(service.aliases)
    else:
        service.print_aliases(service.aliases)

if __name__ == "__main__":
    app()