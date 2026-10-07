
BOLD = "\x1b[1m"
RØD = "\x1b[31m"
GRØNN = "\x1b[32m"
BLÅ = "\x1b[34m"
DEFAULT = "\x1b[0m"

# Returnerer index av valg
def getOpt(opts: list[str]) -> int:
    choice = 0

    for i, opt in enumerate(opts):
        print(f"{BLÅ}{i + 1}{DEFAULT}. {opt}")

    while True:

        try:
            choice = int(input(f"Valg ({BLÅ}1-{len(opts)}{DEFAULT}): "))
            if choice < 1 or choice > len(opts):
                print(f"{RØD}Velg mellom 1-{len(opts)}{DEFAULT}")
                continue

            print(f"{GRØNN + BOLD}{opts[choice - 1]}{DEFAULT}")
            return choice - 1

        except ValueError:
            print(f"{RØD}ikke gyldig valg{DEFAULT}")


# Eksempel
options = [
    "Legg til student",
    "Se alle studenter",
    "Fjern student",
    "Søk etter student",
    "Avslutt"
]

n = getOpt(options)
print(f"Du valgte {options[n]}")