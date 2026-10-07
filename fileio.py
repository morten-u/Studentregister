import student as st
from pathlib import Path
import json

def load(filepath: str) -> list[st.Student]:
    l: list[st.Student] = []

    path = Path(filepath)
    if not path.exists():
        return l
    

    try:

        with open(filepath, "r") as f:
            data = json.load(f)
            
        for s in data:
            student = st.Student(s["f_name"], s["age"], s["course"])
            l.append(student)

        return l
    except Exception as e:
        print(f"Error: klarte ikke lese fil {filepath}\n{e}")
        input("Press enter for å fortsette")
        return l

def write(filepath: str, students: list[st.Student]):

    l: list[dict] = []
    for s in students:
        d = s.toDict()
        l.append(d)

    try:
        with open(filepath, "w") as f:
            json.dump(l, f, indent=4)
    except Exception as e:
        print(f"Error: klarte ikke å skrive til {filepath}\n{e}")

    pass