# Teachers and students are identified by an integer that represents their
# proficiency level.
# Write a method to assign each student to the teacher of the closest level.

# students
# s = [ 1, 5, 8, 14, 56, 12, 0, 98, 3]
# s = [0, 1, 3, 5, 8, 12, 14, 56, 98]

# teachers
# t = [1, 2, 5, 7, 87, 14, 56]
#t = [1, 2, 5, 7, 14, 56, 87]

# you can write to stdout for debugging purposes, e.g.
#
# [(1, 1),(8, 7), (14, 14), (56, 56), (12, 14), (0,1), (98, 87), (3, 2)]
print("This is a debug message")


def teacher_and_student(students, teachers):

    t_s = {}

    for elem in t:
        t_s[elem] = []

    for elem in s:
        diff = float('inf')
        for key in t_s:

            if elem == key:
                teach = key
                break
            curr_d = abs(key-elem)

            if curr_d < diff:
                diff = curr_d
                teach = key

        t_s[teach].append(elem)

    return t_s

  # students
# s = [ 1, 5, 8, 14, 56, 12, 0, 98, 3]
# s = [0, 1, 3, 5, 8, 12, 14, 56, 98]

# teachers
# t = [1, 2, 5, 7, 87, 14, 56]
#t = [1, 2, 5, 7, 14, 56, 87]

"""
def teacher_and_student_v1(students, teachers):

    students.sort()
    teachers.sort()
    teacher_stud = {}

    # storing teachers
    for teacher in teachers:
        teacher_stud[teacher] = []

    teach_i = 0
    stud_i = 0

    while stud_i < len(students) and teach_i < len(teachers):
        diff = abs(students[stud_i] - teachers[teach_i])
        diff_next = abs([teachi_+1])
        if(diff < diff_next):
            teacher[tu].append
            s_i = +1
        else:
            t_1+1
        while:
            curr_d = abs(students[stud_i] - teachers[teach_i])

            if curr_d < diff:
                diff = curr_d

            if curr_d > diff:
                break
            teach_i += 1

        teacher_stud[teachers[teach_i-1]].append(students[stud_i])

        stud_i += 1

    return teacher_stud
"""


def assign_student_to_teachers(students, teachers):

    students.sort()
    teachers.sort()

    teacher_stud = {}

    # storing teachers
    for teacher in teachers:
        teacher_stud[teacher] = []



# students
s = [1, 5, 8, 14, 56, 12, 0, 98, 3]

# teachers
t = [1, 2, 5, 7, 87, 14, 56]

result = teacher_and_student(s, t)
print(result)
