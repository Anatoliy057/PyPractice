from option27.task3.student import Student
from operator import methodcaller
import json
import requests
import random


def to_fixed(num, digits=0):
    return float(f"{num:.{digits}f}")


def from_site():
    _students = []
    with open("students_temp.json", "w", encoding='utf-8') as wf:
        for i in range(20):
            response = requests.get('https://randus.org/api.php').json()
            _student = {}
            desk = {'gender': response['gender']['gender']}
            response = response['name']
            _student['mark'] = to_fixed(random.uniform(2, 5), 1)
            _student['course'] = random.randint(1, 5)
            desk['name'] = response['fname']['normal']
            desk['surname'] = response['lname']['normal']
            desk['patronymic'] = response['patronymic']['normal']
            _student['desk'] = desk
            _students.append(Student.to_student(_student))
            wf.write(json.dumps(_student, ensure_ascii=False))
    return _students


def from_file(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as rf:
        data = json.loads(rf.read())
    _students = []
    for _o in data:
        _students.append(Student.to_student(_o))
    return _students


sw = input("From file? y/n ")

if sw == 'y':
    students = from_file('students.json')
else:
    students = from_site()
x = float(input("Minimal mark: "))
n = int(input("Minimal students: "))
i = 0
expelled = []
remaining = []
for student in students:
    if student.mark() < x:
        expelled.append(student)
    else:
        remaining.append(student)
    i += 1
if len(remaining) < n:
    expelled = sorted(expelled, key=methodcaller('mark'))
    n = len(expelled) - (n - len(remaining))
    i = n
    while i > 0:
        if expelled[i].mark() != expelled[i - 1].mark():
            break
        i -= 1
    remaining = expelled[i:] + remaining

with open('result.txt', "w", encoding='utf-8') as save:
    save.write(str(remaining))
