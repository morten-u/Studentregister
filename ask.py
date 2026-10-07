
BOLD = "\x1b[1m"
RED = "\x1b[31m"
GREEN = "\x1b[32m"
BLUE = "\x1b[34m"
DEFAULT = "\x1b[0m"

# Returnerer index av valg
def getOpt(opts: list[str]) -> int:
    choice = 0

    for i, opt in enumerate(opts):
        print(f"{BLUE}{i + 1}{DEFAULT}. {opt}")

    while True:

        try:
            choice = int(input(f"Valg ({BLUE}1-{len(opts)}{DEFAULT}): "))
            if choice < 1 or choice > len(opts):
                print(f"{RED}Velg mellom 1-{len(opts)}{DEFAULT}")
                continue

            return choice - 1

        except ValueError:
            print(f"{RED}ikke gyldig valg{DEFAULT}")


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