
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

    while True:
        try:
            s.age = int(input("Alder: "))
            break
        except ValueError:
            print("Ugyldig tall, prøv igjen")
    s.course = input("Klasse: ")

    print("Legg til student: ")
    print(f"navn: {s.f_name}, alder: {s.age}, klasse: {s.course}")
    opt = "y"
    opt = input("[Y/n]? ")
    opt = opt.lower()

    if opt.startswith("y") or len(opt) == 0:
        return s
    else:
        return None