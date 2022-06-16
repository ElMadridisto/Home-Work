list_courses_grades_student = []
list_courses_grades_lecturer = []
class Student:
    
    def __init__(self, name, surname, gender, average_grades_student = 0):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grades_list = []
        self.average_grades_student = average_grades_student
        self.list_courses_grades_student = list_courses_grades_student.append(self.grades)

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_cw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_courses:
                lecturer.grades_courses[course] += [grade]
            else:
                lecturer.grades_courses[course] = [grade]
        else:
            return 'Ошибка'
    def average_grades_students(self):
      for courses, grade in self.grades.items():
        self.grades_list += grade
        self.average_grades_student = sum(self.grades_list)/len(self.grades_list)
        
    def __str__(self):
      return f"СТУДЕНТ:\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнюю работу: {self.average_grades_student}\nКурс: {', '.join(self.courses_in_progress)}\nЗавершенный курс: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
       if not isinstance(other, Student):
        print('Not a Student!')
        return
       return self.average_grades_student < other.average_grades_student         
  
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
  def __init__(self, name, surname, average_grades_lecturer = 0):
    super().__init__(name, surname)
    self.average_grades_lecturer = average_grades_lecturer
    self.grades_list = []
    self.grades_courses = {}
    self.list_courses_grades_lecturer = list_courses_grades_lecturer.append(self.grades_courses)
    
  def average_grades(self):
    for course, grade in self.grades_courses.items():
      self.grades_list += grade
      self.average_grades_lecturer = sum(self.grades_list)/len(self.grades_list)
      
    
  def __str__(self):
      return f"ЛЕКТОР:\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades_lecturer}\n"
       
  def __lt__(self, other):
       if not isinstance(other, Lecturer):
        print('Not a Lecture!')
        return
       return self.average_grades_lecturer < other.average_grades_lecturer  
  
class Reviever(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
      return f"ПРОВЕРЯЮЩИЙ:\nИмя: {self.name}\nФамилия: {self.surname}\n"
    

student_1 = Student('Декстер', 'Морган', 'муж')
student_1.courses_in_progress += ['Биология', 'Python']
student_1.finished_courses += ['Git']

student_2 = Student('Брайан', 'Мозер', 'муж')
student_2.courses_in_progress += ['Биология', 'Python']
student_2.finished_courses += ['Git']

lecturer_1 = Lecturer('Артур', 'Митчелл')
lecturer_1.courses_attached += ['Биология']
student_1.rate_cw(lecturer_1, 'Биология', 9)
student_1.rate_cw(lecturer_1, 'Биология', 8)
student_1.rate_cw(lecturer_1, 'Биология', 10)
student_2.rate_cw(lecturer_1, 'Биология', 10)
student_2.rate_cw(lecturer_1, 'Биология', 7)
student_2.rate_cw(lecturer_1, 'Биология', 7)

lecturer_2 = Lecturer('Ханна', 'Маккей')
lecturer_2.courses_attached += ['Python']
student_1.rate_cw(lecturer_2, 'Python', 10)
student_1.rate_cw(lecturer_2, 'Python', 10)
student_1.rate_cw(lecturer_2, 'Python', 9)
student_2.rate_cw(lecturer_2, 'Python', 8)
student_2.rate_cw(lecturer_2, 'Python', 9)
student_2.rate_cw(lecturer_2, 'Python', 10)



mentor_1 = Reviever('Джордан', 'Чейз')
mentor_1.courses_attached += ['Python']
mentor_1.rate_hw(student_1, 'Python', 5)
mentor_1.rate_hw(student_1, 'Python', 9)
mentor_1.rate_hw(student_1, 'Python', 7)
mentor_2 = Reviever('Мария', 'ЛаГуэрта')
mentor_2.courses_attached += ['Биология']
mentor_2.rate_hw(student_1, 'Биология', 8)
mentor_2.rate_hw(student_1, 'Биология', 9)
mentor_2.rate_hw(student_1, 'Биология', 7)

mentor_1 = Reviever('Джордан', 'Чейз')
mentor_1.courses_attached += ['Python']
mentor_1.rate_hw(student_2, 'Python', 10)
mentor_1.rate_hw(student_2, 'Python', 7)
mentor_1.rate_hw(student_2, 'Python', 7)
mentor_2 = Reviever('Мария', 'ЛаГуэрта')
mentor_2.courses_attached += ['Биология']
mentor_2.rate_hw(student_2, 'Биология', 10)
mentor_2.rate_hw(student_2, 'Биология', 9)
mentor_2.rate_hw(student_2, 'Биология', 8)


student_1.average_grades_students()
lecturer_1.average_grades()
student_2.average_grades_students()

student_1.rate_cw(lecturer_2, 'Python', 9)
student_1.rate_cw(lecturer_2, 'Python', 8)
lecturer_2.average_grades()

print(student_1.grades, '\n')
print(student_1, "\n")
print(student_2.grades, '\n')
print(student_2, '\n')
print(mentor_1)
print(mentor_2)
print(lecturer_1.grades_courses, '\n')
print(lecturer_1)
print(lecturer_2.grades_courses, '\n')
print(lecturer_2)

print(student_1<student_2, '\n')

print(lecturer_1<lecturer_2)

#print(list_courses_grades_student)
c = []
d = 0
training_course = input("Введите учебный курс по котору вас интересует оценка: (Python, Биология) ")
def averege_great_course_student(list):
    for student in list:
        if training_course in student:
            for a,b in student.items():
                if a == training_course:
                    for g in b:
                        c.append(g)
            d = sum(c)/len(c)
        else:
             return ('Такого курса нет')
    return f'Средняя оценка по курсу {training_course} состовляет {d}'
print(averege_great_course_student(list_courses_grades_student))

training_course_2 = input("Введите лекционный курс по котору вас интересует оценка: (Python, Биология) ")
def averege_great_course_lecturer(list):
    for lecturer in list:
        for a,b in lecturer.items():
            if a == training_course_2:
               for g in b:
                  c.append(g)
                  d = sum(b)/len(b)
                  return f'Средняя оценка по лекциям {training_course_2} состовляет {d}'
            else:
                    return f'Нет такого курса'

print(averege_great_course_lecturer(list_courses_grades_lecturer))

