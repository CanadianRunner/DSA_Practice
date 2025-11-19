# Write your solution here

def add_student(students: dict, name: str):
  if name not in students:
    students[name] = {
    "courses": []
    }

def print_student(students: dict, name: str):
  if name not in students:
    print(f"{name}: no such person in the database")
    return
  
  student = students[name]
  courses = student["courses"]

  print(f"{name}:")

  if not courses:
    print(" no completed courses")
    return
  
  print(f" {len(courses)} completed courses:")

  total = 0
  for course in courses:
    course_name = course[0]
    grade = course[1]
    print(f"  {course_name} {grade}")
    total += grade

  average = total / len(courses)
  print(f" average grade {average:.1f}")

def add_course(students: dict, name: str, course: tuple):
    course_name, grade = course

    if grade == 0:
        return

    student = students[name]
    courses = student["courses"]

    for i, (existing_name, existing_grade) in enumerate(courses):
        if existing_name == course_name:
            if grade > existing_grade:
                courses[i] = (course_name, grade)
            return 

    courses.append((course_name, grade))

def summary(students: dict):
  student_count = len(students)
  print(f"students {student_count}")

  #Calc/access who has completed the most courses
  most_courses = 0
  name_most_courses = None
  for name, info in students.items():
    courses = info["courses"]
    course_count = len(courses)

    if course_count > most_courses:
        most_courses = course_count
        name_most_courses = name

  print(f"most courses completed {most_courses} {name_most_courses}")

  #Calc/access who has the best average grade
  best_grade = 0.0
  name_best_grade = None

  for name, info in students.items():
    courses = info["courses"]
    if not courses:
        continue

    total = 0
    for course in courses:
        grade = course[1]
        total += grade

    average = total / len(courses)

    if average > best_grade:
        best_grade = average
        name_best_grade = name

  print(f"best average grade {best_grade} {name_best_grade}")

if __name__ == "__main__":
  students = {}
  add_student(students, "Peter")
  add_student(students, "Eliza")
  add_course(students, "Peter", ("Data Structures and Algorithms", 1))
  add_course(students, "Peter", ("Introduction to Programming", 1))
  add_course(students, "Peter", ("Advanced Course in Programming", 1))
  add_course(students, "Eliza", ("Introduction to Programming", 5))
  add_course(students, "Eliza", ("Introduction to Computer Science", 4))
  summary(students)