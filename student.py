import ask

class Student:
    f_name: str
    age: int
    course: str
    def __init__(self, f_name="", age=0, course="") -> None:
        self.f_name = f_name
        self.age = age
        self.course = course


def getStudent():
    print("--- Legg til student ---")

    s = Student()
    s.f_name = input("Fornavn: ")
    s.age = ask.getInt("Alder: ")
    s.course = input("Klasse: ")

    if ask.confirm(f"Legg til {s.f_name} som student?"):
        return s
    else:
        return None


def showStudents(students: list[Student]):
    print("--- Vis alle studenter ---")
    if (len(students) == 0):
        print("Ingen studenter lagt til")
        input("Press enter for å returnere: ")
        return

    n = f"{ask.BOLD}NAVN{ask.DEFAULT}"
    a = f"{ask.BOLD}ALDER{ask.DEFAULT}"
    c = f"{ask.BOLD}KLASSE{ask.DEFAULT}"
    print(f"{n:<18} | {a:<15} | {c}")
    for s in students:
        print(f"{s.f_name:<10} | {s.age:<7} | {s.course}")
    input("Press enter for å returnere: ")

def searchStudents(students: list[Student]):
    print("--- Søk etter student ---")
    options = [
        "Navn",
        "Alder",
        "Klasse"
    ]

    print(f"Søk valg")
    choice = ask.getOpt(options)

    name: str = ""
    age: int = 0
    course: str = ""

    match choice:

        case 0: # Navn
            name = input("Navn: ")
            name = name.lower()

            for s in students:
                if s.f_name.lower().startswith(name):
                    print(f"{s.f_name:<10} | {s.age:<5} | {s.course}")

        case 1: # Alder
            age = ask.getInt("Alder: ")
            for s in students:
                if s.age == age:
                    print(f"{s.f_name:<10} | {s.age:<5} | {s.course}")
                    
        case 2: # Klasse
            course = input("Klasse: ")
            course = course.lower()

            for s in students:
                if s.course.lower().startswith(course):
                    print(f"{s.f_name:<10} | {s.age:<5} | {s.course}")

    input("Press enter for å returnere: ")


def removeStudent(students: list[Student]):
    print("--- Fjern student ---")
    for i, s in enumerate(students):
        print(f"{ask.RED}{i + 1}{ask.DEFAULT}. {s.f_name:<10} {s.course}")

    rm_idx = 0
    while rm_idx < 1 or rm_idx > len(students):
        rm_idx = ask.getInt(f"Fjern student ({ask.RED}1-{len(students)}{ask.DEFAULT}): ")
    rm_idx -= 1
    if ask.confirm(f"Fjern {ask.RED}{students[rm_idx].f_name}{ask.DEFAULT}"):
        students.remove(students[rm_idx])

def studentCount(students: list[Student]):
    print("--- Antall studenter ---")
    print(f"Total antall: {len(students)}")
    input("Press enter for å returnere: ")
