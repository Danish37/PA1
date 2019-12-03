class CalUtils:
    def __init__(self,names,heights,totalStudentHeight,totalStudentCount):
        self.names = names
        self.heights = heights
        self.totalStudentHeight = totalStudentHeight
        self.totalStudentCount = totalStudentCount
    def calAvgHeight(self):
        avgHeight = self.totalStudentHeight/self.totalStudentCount
        return avgHeight

with open('C:/Users/T05-17/PycharmProjects/PA1/listOfStudentHeight.txt') as f:
    myArray = f.readlines()

totalStudents = 0
totalHeights = 0
for line in myArray:
    myList = line.split()
    myName = myList[0]
    myHeight = float(myList[1])
    totalHeights += myHeight
    totalStudents += 1
    person = CalUtils(myName,myHeight,totalHeights,totalStudents)
    avgHeight = person.calAvgHeight()
print('Student average height is',round(avgHeight,2),'m for',totalStudents,'students')

yourName = input("Enter new student name: ")
yourHeight = input("Enter student height(in metres): ")

try:
    yourHeight = float(yourHeight)
except:
    print("Please enter height is numerical value")
    yourHeight = input("Enter student height(in metres): ")
    yourHeight = float(yourHeight)

totalHeights += yourHeight
totalStudents += 1
newPerson = CalUtils(yourName,yourHeight,totalHeights,totalStudents)
newavgHeight = newPerson.calAvgHeight()
print('Student average height is',round(newavgHeight,2),'m for',totalStudents,'students')