import getOptions as opt
import student as st

def clear():                # \x1b[2J = tømmer skjermen
    print("\x1b[2J\x1b[H")  # \x1b[H  = sender markøren til start

def main():

    students: list[st.Student] = []
    options = [
        "Legg til student",
        "Vis alle studenter",
        "Søk etter student",
        "Fjern student",
        "Vis antall studenter",
        "Avlsutt"
    ]

    running = True
    while running:

        clear()
        choice = opt.getOpt(options)

        match choice:
            case 0: # Legg til student
                s = st.getStudent()
                if s == None:
                    continue
                print(f"Student mottat!")
                students.append(s)

            case 1: # Vis alle studenter
                pass
            case 2: # Søk etter student
                pass
            case 3: # Fjern student
                pass
            case 4: # Vis antall studenter
                pass
            case 5: # Avslutt
                running = False







if __name__ == "__main__":
    main()