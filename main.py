string_task_1 = 'слово другое слово теорема теорема слово банан банан слово другое слово'
dict_task_2 = {'Ivan': 5, 'Maria': 4, 'Anna': 5, 'Petr': 3}
dict_task_3_1 = {'яблоко': 10, 'банан': 5, 'апельсин': 3}
dict_task_3_2 = {'банан': 7, 'апельсин': 2, 'виноград': 4}
dict_task_4 = {'Иван': ['математика', 'физика'], 'Мария': ['химия', 'биология'], 'Петр': ['математика', 'информатика'], 'Анна': ['биология', 'физика']}


def task_1(user_string):
    words = string_task_1.lower().split(' ')
    words_num = {}
    for i in set(words):
        words_num[i] = words.count(i)
    return words_num


def task_2(students_dict):
    marks = set(students_dict.values())
    marks_dict = {}
    for mark in marks:
        students_list = []
        for key, value in students_dict.items():
            if mark == value:
                students_list.append(key)
        marks_dict[mark] = students_list
    return marks_dict


def task_3(dict_1, dict_2):
    keys_set = set(dict_1.keys()) | set(dict_2.keys())
    total_dict = {}
    for i in keys_set:
        if dict_1.get(i) is None:
            total_dict[i] = dict_2.get(i)
        elif dict_2.get(i) is None:
            total_dict[i] = dict_1.get(i)
        else:
            total_dict[i] = dict_1.get(i) + dict_2.get(i)
    return total_dict


def task_4(students, lesson_name):
    student_on_lesson = []
    for student, lessons in students.items():
        if lesson_name in lessons:
            student_on_lesson.append(student)
    return student_on_lesson


print(task_1(string_task_1))
print(task_2(dict_task_2))
print(task_3(dict_task_3_1, dict_task_3_2))
print(task_4(dict_task_4, 'математика'))
