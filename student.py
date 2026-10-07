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