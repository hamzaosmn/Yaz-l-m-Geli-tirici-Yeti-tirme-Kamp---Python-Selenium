listStudents = ["Student A","Student B"]
print(listStudents)

def addStudent(name):
    listStudents.append(input("Name Surname:"))
addStudent("")
print(listStudents)

def deleteStudent(name):
    listStudents.remove(input("Name Surname:"))
deleteStudent("")
print(listStudents)

def addManyStudent():
    listStudents.extend([input("Name Surname:")])
addManyStudent()
print(listStudents)

def students():
    for student in listStudents:
        print(student)
students()

def indexStudents():
    for i in listStudents:
        print(listStudents.index(i))
indexStudents()


def deleteMultipleStudents():

    while True:
        nameeSurname = input("Name Surname:")
        deleteNameSurname = f"{nameeSurname}"
        listStudents.remove(deleteNameSurname)
        break
deleteMultipleStudents()
print(listStudents)


