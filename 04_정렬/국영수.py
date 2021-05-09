N = int(input())
students = list()
result = list()

for _ in range(N):
    inputs = list(map(str, input().split()))
    students.append((inputs[0], int(inputs[1]), int(inputs[2]), int(inputs[3])))

students = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])