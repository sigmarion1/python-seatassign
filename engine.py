
import random


nMaleStudent = int(input("남학생 숫자 입력"))
nFemaleStudent = int(input("여학생 숫자 입력"))

aMaleStudent = [x+1 for x in range(nMaleStudent)]
aFemailStudent = [x+31 for x in range(nFemaleStudent)]

aAllStudent = aMaleStudent + aFemailStudent
aAssignSeat = list()

while aAllStudent:
    temp = random.choice(aAllStudent)
    aAllStudent.remove(temp)
    aAssignSeat.append(temp)

for i in range(int(len(aAssignSeat)/5)):
    x = list()
    for j in range(5):
        x.append(aAssignSeat[i*5 + j])

    print(x)


