from statistics import mean
if __name__ == "__main__":
    StudentMarks = dict()
    N = int(input("Enter count of students = "))
    for i in range(N):
        InputInformation = str(input("Write line with student Name and Marks: ")).split(' ')
        InputName, InputMarks = InputInformation[0], map(float, InputInformation[1:])
        StudentMarks[InputName] = InputMarks
    YourChoice = input("Needed name of student: ")
    if YourChoice in StudentMarks.keys():
        print("%.2f" % mean(StudentMarks[YourChoice]))
