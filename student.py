
class Student:
    f_name: str
    age: int
    course: str
    def __init__(self, f_name="", age=0, course="") -> None:
        self.f_name = f_name
        self.age = age
        self.course = course

GREEN = "\x1b[32m"
DEFAULT = "\x1b[0m"

def getStudent():
    print("--- Legg til student ---")

    s = Student()
    s.f_name = input("Fornavn: ")

    while True:
        try:
            s.age = int(input("Alder: "))
            break
        except ValueError:
            print("Ugyldig tall, prøv igjen")
    s.course = input("Klasse: ")

    print("Legg til student: ")
    print(f"navn: {s.f_name}, alder: {s.age}, klasse: {s.course}")
    opt = "j"
    opt = input(f"[{GREEN}J{DEFAULT}/n]? ")
    opt = opt.lower()

    if opt.startswith("j") or len(opt) == 0:
        return s
    else:
        return None

def showStudents(students: list[Student]):
    print("--- Vis alle studenter ---")
    if (len(students) == 0):
        print("Ingen studenter lagt til")
        input("Press enter for å returnere: ")
        return

    n = "NAVN"
    a = "ALDER"
    c = "KLASSE"
    print(f"{n:<10} | {a:<5} | {c}")
    for s in students:
        print(f"{s.f_name:<10} | {s.age:<5} | {s.course}")
    input("Press enter for å returnere: ")