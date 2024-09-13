from tabulate import tabulate

def print_alias(alias):
        print(f"{alias.email}")
        
def print_aliases(aliases):
    for alias in aliases:
        print(f"{alias.email}")

def pretty_print_aliases(aliases):
    lines = []
    for alias in aliases:
        lines.append([alias.id, alias.email, alias.pinned])
    print(tabulate(lines, headers=["ID","Mail", "Pinned"], tablefmt="github"))