import classes
 
admin = []
admin_counter = 0

students = []
student_counter = 0

faculty = []
faculty_counter = 0

courses = []
course_counter = 0


def load_admin_details():
    global admin_counter
    al = open("adminlogin.txt", "r")
    Admin = []
    for x in range(1):
        a_obj = al.readline()
        a_obj = a_obj.replace("\n", "")

        array = a_obj.split("-")
        for word in array:
            Admin.append(word)
        admin.append('a' + str(admin_counter))
        admin[x] = classes.Admin()
        admin_counter += 1
        admin[x].load_admin_login(array)
        Admin.clear()

def load_stu():
  global student_counter
  sl = open("student_info.txt", "r")
  
  for x in range(7):
    s_obj = sl.readline()
    s_obj = s_obj.replace("\n", "")
    array = s_obj.split("-")
    courses = array[4]
    courses = courses.split(",")
    students.append("s" + str(student_counter))
    students[student_counter] = classes.Student()
    students[student_counter].load_student(array, courses)
    student_counter += 1

def load_courses():
  global course_counter
  sl = open("courses.txt", "r")
  
  for x in range(5):
    s_obj = sl.readline()
    s_obj = s_obj.replace("\n", "")
    array = s_obj.split("-")
    students = array[3].split(",")
    courses.append("c" + str(course_counter))
    courses[course_counter] = classes.Courses()
    courses[course_counter].load_courses(array, students)
    course_counter += 1

def load_faculty():
  global faculty_counter
  sl = open("faculty_info.txt", "r")
  
  for x in range(5):
    s_obj = sl.readline()
    s_obj = s_obj.replace("\n", "")
    array = s_obj.split("-")
    courses = array[4].split(",")
    faculty.append("f" + str(faculty_counter))
    faculty[faculty_counter] = classes.Faculty()
    
    faculty[faculty_counter].load_faculty(array, courses)
    faculty_counter += 1
    
def admin_login():
    logged_in = False
    print("-------Admin Login------")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if admin[0].user_name == username and admin[0].password == password:
        logged_in = True
    return logged_in


  
def student_login():
  logged_in = False
  print("------Student Login-----")
  student_username = input("Enter your username: ")
  student_password = input("Enter your password: ")
  if students[0].username == student_username and students[0].password == student_password:
    logged_in = True
  return logged_in

load_admin_details()
load_stu()
load_courses()
load_faculty()


while(1):
  print('------------------------')
  print('Enter status to login')
  print('------------------------')
  print('1-Admin')
  print('2-Faculty')
  print('3-Student')
  print('4-Close Program')
  status = input('Enter Here: ')
  print('------------------------')
  if status =='1':
    print("Enter Admin Username and Password")
    print('------------------------')
    if admin_login() == True:
      print("\nWelcome to Carlos-Board!")
      while True:
        print("----------Menu----------")
        print("1 - Create student")
        print("2 - Create Faculty")
        print("3 - Create course")
        print('4 - Logout')
        choice = input("Enter your choice: ")
        print('------------------------')
        if choice == "1":
            students.append("s" + str(len(students)))
            students[student_counter] = classes.Student()
            students[student_counter].create_stu()
        elif choice == "2":
            faculty.append("f" + str(len(faculty)))
            faculty[faculty_counter] = classes.Faculty()
            faculty[faculty_counter].create_fac()
        elif choice == "3":
            courses.append("c" + str(len(courses)))
            courses[course_counter] = classes.Courses()
            courses[course_counter].create_course()
        elif choice =='4':
          break
    else:
      print("Wrong username or password.\n")
  elif status=='2':
    print("Enter Faculty Username and Password")
    print('------------------------')
    faculty_username = input('Enter Username:')
    faculty_password = input('Enter Password:')
    for z in range(len(faculty)):
      if faculty[z].username == faculty_username and faculty[z].password == faculty_password:
        print("\nWelcome to Carlos-Board!")
        while True:
          print("----------Menu----------")
          print("1 - Grade")
          print('2 - Courses Taught')
          print("3 - Create announcement")
          print('4 - Logout')
          teacher_choice = input('Enter Here:')
          if teacher_choice =='1':
            print("Which student do you want to grade?: ")
            for x in range(len(courses)):
              for y in range(len(faculty[z].courses)):
                if courses[x].CID == faculty[z].courses[y]:
                  print(courses[x].students)
            stu_to_grade = input("Enter the Student: ")
            for x in range(len(students)):
              if students[x].name == stu_to_grade:
                new_grade = input("Enter their new grade for the course: ")
                students[x].courses[courses[0].name] = new_grade
                
          elif teacher_choice == '2':
            print(faculty[z].courses)
          elif teacher_choice == '3':
            for x in range(len(courses)):
              for y in range(len(faculty[0].courses)):
                if courses[x].CID == faculty[z].courses[y]:
                  courses[x].create_announcement()
          elif teacher_choice == '4':
            break 
          
  elif status =='3':
    print("Enter Student Username and Password")
    print('------------------------')
    sl = classes.Student()
    student_username = input("Enter Username:")
    student_password = input('Enter Password:')
    for w in range(len(students)):
      if students[w].username == student_username and students[w].password == student_password:
        print("\nWelcome to Carlos-Board!")
        while True:  
          print('1 - Register for a course')
          print('2 - View Courses')
          print('3 - logout')
          studentchoice = input("Enter Here: ")
          if studentchoice == '1':
            stu1 = classes.Student()
            cour_choice = input("Enter the course ID you want to register for: ")
            for x in range(len(courses)):
              if cour_choice == courses[x].CID:
                students[w].register_for_course(courses[x])
          elif studentchoice == '2':
            keys = list(students[w].courses.keys())
            for x in range(len(courses)):
                for y in range(len(keys)):
                  if courses[x].name == keys[y]:
                    print()
                    courses[x].display_info()
                    print("Grade:", students[w].courses[courses[x].name])
                    print()
              
          elif studentchoice == '3':
            break
    
        
  elif status =='4':
    break
      
  else:
      print('ERROR Invalid Entry')
      print('------------------------')
          

