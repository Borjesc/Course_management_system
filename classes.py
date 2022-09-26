class Admin:
  def __init__(self):
    self.username = ""
    self.password = ""

  def load_admin_login(self, fac):
    self.user_name = fac[0]
    self.password = fac[1]

class Student:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.SID = ""
        self.name = ""
        self.courses = {}

    def load_student_login(self, students):
        self.username = students[0]
        self.password = students[1]
  
    def display_info(self):
        print("ID:,", self.SID)
        print("Name:", self.name)
        print("Courses:", self.courses)

    def create_stu(self):
        self.username = input("Enter the username of the student: ")
        self.password = input("Enter the password of the student: ")
        self.SID = input("Enter the student ID: ")
        self.name = input("Enter the students name: ")


    def register_for_course(self, course):
        self.courses[course.name] = "A"
        course.students.append(self.name)
        print(course.students)

    def load_student(self, stu, Courses):
      self.name = stu[0]
      self.username = stu[1]
      self.password = stu[2]
      self.SID = stu[3]
      for x in range(0, len(Courses), 2):
        self.courses[Courses[x]] = Courses[x+1]
      
      pass


class Faculty:
    def __init__(self):
        self.FID = ""
        self.name = ""
        self.courses = []
        self.username = "hi"
        self.password = "password"

    def display_info(self):
        print("ID:", self.FID)
        print("Name", self.name)
        print("Course:", self.courses)

    def create_fac(self):
        self.FID = input("Enter the ID of the faculty: ")
        self.name = input("Enter the name of the faculty: ")
        self.username = input("Enter the username for the faculty: ")
        self.password = input("Enter the password for the faculty: ")

    def register_for_course(self, course):
        self.courses.append(course.CID)
        course.faculty = self.FID
      
    def load_faculty(self, fac, courses):
      self.name = fac[0]
      self.username = fac[1]
      self.password = fac[2]
      self.FID = fac[3]
      self.courses = courses[:]


class Courses:
    def __init__(self):
        self.name = ""
        self.CID = ""
        self.students = []
        self.faculty = ""
        self.exams = []
        self.announcements = []

    def display_info(self):
        print("Course Name:", self.name)
        print("Course ID:", self.CID)
        
        print("Faculty Member:", self.faculty)
        print("Announcements:")
        if len(self.announcements) > 0:
            for x in range(len(self.announcements)):
                print("-" + self.announcements[x])
              

    def create_announcement(self):
        a = open(f'{self.name}_announcements', "a")
        announcement = input("Enter the announcement ")
        a.write(announcement + "\n")
        self.announcements.append(announcement + "\n")

    def create_course(self):
        self.name = input("Enter the name of the course: ")
        self.CID = input("Enter the course ID: ")

    def load_courses(self, cour, stu):
      self.name = cour[0]
      self.CID = cour[1]
      self.faculty = cour[2]
      self.students = stu[:]
