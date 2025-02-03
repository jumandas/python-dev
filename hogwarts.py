#list

students = ["Hermoine", "Harry","Ron"]
for i in students:
    print(i)
    

print(students[0])

#len
for i in range(len(students)):
    print(i + 1 ,students[i])
    
#1 Hermoine
#2 Harry
#3 Ron
    
#dict
student = {"Hermoine":"Gryffindor",
           "Harry":"Gryffindor",
           "Ron":"Gryffindor",
           "Draco":"Slytherin"}

print(student["Hermoine"])

for stud in student:
    print(stud,student[stud],sep=", ")
    
    
#huge dict with key and value 
#None Keyword- Absent of value

students=[
    {"name":"Hermoine","house":"Gryffindor","patronus":"otter"},
    {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
    {"name":"Ron","house":"Gryffindor","patronus":"Jack"},
    {"name":"Draco","house":"Slytherin","patronus":None}
]

for stud in students:
    print(stud["name"],stud["house"],stud["patronus"],sep= " , ")