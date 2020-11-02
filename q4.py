class CDU:
    'Common base class for CDU colleges'
    StudentCount = 0
    def __init__(self):
        print("CDU class initiated")
 
    def displayStudentCount(self):
        print(f"\n Total students are: {CDU.StudentCount} \n")
 
class CollegeOfIT(CDU):
    Building_address = "Purple 12, CDU Casuarina Campus"
 
    def __init__(self, name, course):
        print("College of IT class initiated \n")
        self.name = name
        self.course = course
        CDU.StudentCount += 1
 
class CollegeOfEng(CDU):
    Building_address ="Blue 9(may be), CDU Casuarina Campus"
 
    def __init__(self, name, course):
        print("College of Engineering class initiated \n")
        self.name = name
        self.course = course
        CDU.StudentCount += 1
 
class CollegeOfEnv(CDU):
    Building_address = "ABC 123, CDU Casuarina Campus \n"
 
    def __init__(self, name, course):
        print("College of Environment class initiated \n")
        self.name = name
        self.course = course
        CDU.StudentCount += 1
 
student1 = CollegeOfIT("tony ","Bachelor of IT")
student2 = CollegeOfIT("raj ", "Master of IT")
 
print(f"Building address for {student1.name} is : {student1.Building_address}")
print(f"Building address for {student2.name} is : {student2.Building_address}")
 
student3 = CollegeOfEng("1st student of Eng","Bachelor Engineering")
student4 = CollegeOfEng("2nd student of Eng", "Master of Engineering")
 
print( f"Building address for {student3.name} is : {student3.Building_address}")
print(f"Building address for {student4.name} is : {student4.Building_address}")
 
student5 = CollegeOfEnv("1st student of Env","Bachelor of Environmental science")
student6 = CollegeOfEnv("2nd student of Env", "Master of Disaster management")
 
print(f"Building address for {student5.name} is : {student5.Building_address}")
print(f"Building address for {student6.name} is : {student6.Building_address}")
 
parentObject = CDU()
parentObject.displayStudentCount()