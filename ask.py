
BOLD = "\x1b[1m"
RED = "\x1b[31m"
GREEN = "\x1b[32m"
BLUE = "\x1b[34m"
DEFAULT = "\x1b[0m"

def confirm(prompt: str) -> bool:
    print(prompt)
    opt = input(f"[{GREEN}J{DEFAULT}/n]? ")
    if len(opt) == 0 or opt.lower().startswith("j"):
        return True

    return False


def getInt(prompt: str) -> int:
    i = 0
    while True:
        try:
            tmp = input(prompt)
            i = int(tmp)
            return i
        except ValueError:
            print(f"{RED}{tmp} er ikke gyldig tall{DEFAULT}")

# Returnerer index av valg
def getOpt(opts: list[str]) -> int:
    choice = 0

    for i, opt in enumerate(opts):
        print(f"{BLUE}{i + 1}{DEFAULT}. {opt}")

    while True:

        choice = getInt(f"Valg ({BLUE}1-{len(opts)}{DEFAULT}): ")

        if choice < 1 or choice > len(opts):
            print(f"{RED}Velg mellom 1-{len(opts)}{DEFAULT}")
            continue

        return choice - 1 # Trekk fra 1 for å få riktig index
        


# Eksempel
# options = [
#     "Legg til student",
#     "Se alle studenter",
#     "Fjern student",
#     "Søk etter student",
#     "Avslutt"
# ]

# n = getOpt(options)
# print(f"Du valgte {options[n]}")