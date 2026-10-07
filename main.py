import ask
import student as st

def clear():                # \x1b[2J = tømmer skjermen
    print("\x1b[2J\x1b[H")  # \x1b[H  = sender markøren til start

def main():

    students: list[st.Student] = [
        st.Student("Morten", 33, "Systemutvikling og Programmering"),
        st.Student("Michael", 32, "Systemutvikling og Programmering"),
        st.Student("Chris",   28, "It Drift og Sikkerhet"),
        st.Student("Kenneth", 33, "It Drift og Sikkerhet"),
        st.Student("Eren-Kevin", 30, "It Drift og Sikkerhet")
    ]
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
        print("--- STUDENTREGISTER ---")
        choice = ask.getOpt(options)

        match choice:
            case 0: # Legg til student
                clear()
                s = st.getStudent()
                if s:
                    students.append(s)

            case 1: # Vis alle studenter
                clear()
                st.showStudents(students)

            case 2: # Søk etter student
                clear()
                st.searchStudents(students)
                pass
            case 3: # Fjern student
                clear()
                st.removeStudent(students)
                pass
            case 4: # Vis antall studenter
                pass
            case 5: # Avslutt
                running = False
                clear()







if __name__ == "__main__":
    main()