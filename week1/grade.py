'''

Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку по всем абитуриентам.

В качестве ответа на задание прикрепите полученный файл со средними оценками.

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
Sample Input:

Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85
Sample Output:

85.0
94.0
71.666666667
81.0 84.0 85.666666667
'''

dir = 'D:\GitHub\learning_python\week1\dataset_3363_4.txt'

with open(dir, 'r') as f:
    text = f.read().split('\n')


def clean_text(text):
    f_text = []
    for i in range(len(text)):
        if text[i] == '':
            del text[i]
    for student in text:
        f_text.append(student.split(';'))
    return f_text


def grade_average_students(text):
    grade = []
    text = clean_text(text)
    for student in text:
        grade.append(
            (int(student[1]) + int(student[2]) + int(student[3])) / 3
        )

    for j in grade:
        print(j)


def grade_average_subj(text, subj):
    grade_average = 0
    text = clean_text(text)
    if subj == 'math':
        i = 1
    elif subj == 'phys':
        i = 2
    else:
        i = 3
    for j in text:
        grade_average += int(j[i])
    print(grade_average / len(text), end=' ')


grade_average_students(text)
grade_average_subj(text, 'math')
grade_average_subj(text, 'phys')
grade_average_subj(text, 'rus')
