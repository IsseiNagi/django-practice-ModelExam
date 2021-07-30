from django import setup
import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
setup()

from ModelApp.models import Students, Classes, Tests, TestResults


class_name_list = [
    '1組',
    '2組',
    '3組',
    '4組',
    '5組',
    '6組',
    '7組',
    '8組',
    '9組',
    '10組',
    ]

stundent_list = [
    'student_A',
    'student_B',
    'student_C',
    'student_D',
    'student_E',
    'student_F',
    'student_G',
    'student_H',
    'student_I',
    'student_J',
]
# !リスト内包表記でかけた。クラスネームもできたかもしれない。
# ! class_names = ['student' + c for c in 'ABCDEFGHIJ']

test_list = ['国語', '算数', '社会']


# テストテーブルにデータを作成
for test in test_list:
    t = Tests(name=test)
    t.save()

# クラステーブルと、それに紐づく生徒テーブルにデータを作成
for class_name in class_name_list:
    class_object = Classes(name=class_name)
    class_object.save()
    for student in stundent_list:
        student_object = Students(
            class_name=class_object,
            name=student,
            grade=1)
        student_object.save()

# 生徒テーブルとテストテーブルからデータを取得して、それらを使って結果テーブルにデータを作成
students = Students.objects.all()
tests = Tests.objects.all()

for student in students:
    for test in tests:
        results = TestResults(
            student=student,
            test=test,
            score=random.randint(50, 100)
        )
        results.save()
