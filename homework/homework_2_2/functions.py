import json


def load_students():  # Загружает список студентов из файла
    file = open("students.json")
    return json.load(file)


def load_professions():  # Загружает список профессий из файла
    file = open("professions.json")
    return json.load(file)


def get_student_by_pk(pk):  # Получает словарь с данными студента по его pk
    students = load_students()
    for student in students:
        if pk == student['pk']:
            return student




def get_profession_by_title(title):  # Получает словарь с инфо о профессии по названию
    professions = load_professions()
    for profession in professions:
        if title == profession["title"]:
            return profession


def check_fitness(student, profession=str):
    result = {}
    b = set(get_student_by_pk(student)["skills"])
    a = set(get_profession_by_title(profession)["skills"])
    result[get_student_by_pk(student)["full_name"]] = get_student_by_pk(student)["skills"]
    result["lacks"] = list(a.difference(b))
    result['aa'] = list(a.intersection(b))
    result["fit_percent"] = int(100 - (100 / len(get_profession_by_title(profession)["skills"]) * len(result["lacks"])))
    return result


def main():
    student = int(input("Введите номер студента: "))
    a = (get_student_by_pk(student))
    if a:
        print(f'{a["full_name"]}\nЗнает {", ".join(a["skills"])}')
        profession = input(f'Выберите специальность для оценки студента {a["full_name"]}: ')
        prof = (get_profession_by_title(profession))
        if prof:
            d = check_fitness(student, profession)
            print(f'Пригодность: {d["fit_percent"]}%\n{a["full_name"]} знает {", ".join(d["aa"])}\n{a["full_name"]} не знает {", ".join(d["lacks"])}')
        else:
            print("нет такой специальности")
    else:
        print('нет такого студента')

main()