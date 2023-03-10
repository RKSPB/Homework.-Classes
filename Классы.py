class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.stud_all_grades = []

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.course_taught and grade >0 and grade <11:       
            lecturer.lect_all_grades.append(grade)
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]                
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating    

    def __str__(self):
        res = (
            f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {sum(self.stud_all_grades) / len(self.stud_all_grades) }
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)} '''
)  
        return res       
    

    def __lt__(self, foe):
        if not isinstance(foe, Student): 
            return
        if sum(foe.stud_all_grades) / len(foe.stud_all_grades) < sum(self.stud_all_grades) / len(self.stud_all_grades):
            self.status = f'Студент {self.surname} имеет большую среднюю оценку'
        else:
            self.status = f'Студент {self.surname} имеет меньшую среднюю оценку'



        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
       
                  
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.course_taught = []
        self.lect_all_grades = []
        
    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating   

    def __str__(self):
        res = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.av_rating()} '''  
        return res
    
  
    def __lt__(self, foe):
        if not isinstance(foe, Lecturer): 
            return
        if sum(foe.lect_all_grades) / len(foe.lect_all_grades) < sum(self.lect_all_grades) / len(self.lect_all_grades):
            self.status = f'Лектор {self.surname} имеет большую среднюю оценку'
        else:
            self.status = f'Лектор {self.surname} имеет меньшую среднюю оценку'
    
    

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
 
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress and grade >0 and grade <11:
            student.stud_all_grades.append(grade)
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        res = f'Имя: {self.name} \n' \
        f'Фамилия: {self.surname}'
        return res
    

        
# Заданные значения для объектов классов
a_student = Student('Василий', 'Васильев', 'м')
a_student.courses_in_progress += ['Анатомия']
a_student.finished_courses += ['Химия', 'Гистология', 'Морфология', 'Физика']

b_student = Student('Маша', 'Машевна', 'ж')
b_student.courses_in_progress += ['Биохимия']
b_student.finished_courses += ['Физика', 'Морфология']

a_lecturer = Lecturer('Профессор', 'Петров')
a_lecturer.course_taught += ['Морфология', 'Гистология']

b_lecturer = Lecturer('Профессор', 'Кошкин')
b_lecturer.course_taught += ['Физика', 'Химия']
 
a_reviewer = Reviewer('Ассистент', 'Ассистентович')
b_reviewer = Reviewer('Ординатор', 'Ординаторович')

 
 # Применение методов
a_student.rate_hw(a_lecturer, 'Гистология', 9)
a_student.rate_hw(a_lecturer, 'Морфология', 7)
a_student.rate_hw(b_lecturer, 'Химия', 10)
a_student.rate_hw(b_lecturer, 'Физика', 9)

b_student.rate_hw(a_lecturer, 'Гистология', 7)
b_student.rate_hw(a_lecturer, 'Морфология', 8)
b_student.rate_hw(b_lecturer, 'Химия', 9)
b_student.rate_hw(b_lecturer, 'Физика', 8)

a_reviewer.rate_hw(a_student, 'Анатомия', 7)
b_reviewer.rate_hw(a_student, 'Анатомия', 10)
a_reviewer.rate_hw(a_student, 'Анатомия', 8)
b_reviewer.rate_hw(a_student, 'Анатомия', 7)

a_reviewer.rate_hw(b_student, 'Биохимия', 10)
b_reviewer.rate_hw(b_student, 'Биохимия', 9)
a_reviewer.rate_hw(b_student, 'Биохимия', 10)
b_reviewer.rate_hw(b_student, 'Биохимия', 10)



b_student < a_student
a_lecturer < b_lecturer



print(a_student)
print()
print(b_student)
print()
print(b_student.status)
print()
print(a_lecturer)
print()
print(b_lecturer)
print()
print(a_lecturer.status)
print()
print(a_reviewer)
print(b_reviewer)

student_list = [a_student, b_student]
lecturer_list = [a_lecturer, b_lecturer]
reviewer_list = [a_reviewer, b_reviewer]

def average_rating_for_students(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_sum_rating = stud.av_rating_for_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return f'Средняя оценка студентов за курс {course}: {average_rating} баллов'

def average_rating_for_lectures(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_sum_rating = stud.av_rating_for_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return f'Средняя оценка лекторов за курс {course}: {average_rating} баллов'

print()
print(average_rating_for_students('Анатомия', student_list))
print(average_rating_for_lectures('Гистология', lecturer_list))
