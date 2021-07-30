from django import setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
setup()

from ModelApp.models import Students, Classes, Tests, TestResults


# データ取得
# id=2の生徒の名前と、テスト科目、点数
results = TestResults.objects.filter(student__id=2).all()
for result in results:
    print(result.student.name, result.test.name, f'{result.score}点')

# 各クラスの平均点、合計点、最高得点、最低得点
# GROUP_BY クラス名、テスト名
from django.db.models import Max, Min, Avg, Sum

for class_summary in Classes.objects.values(
    'name', 'students__testresults__test__name').annotate(
        平均点=Avg('students__testresults__score'),
        合計得点=Sum('students__testresults__score'),
        最高得点=Max('students__testresults__score'),
        最低得点=Min('students__testresults__score'),
        ):
    print(
        class_summary['name'],
        class_summary['students__testresults__test__name'],
        f'{class_summary["平均点"]}点',
        f'{class_summary["合計得点"]}点',
        f'{class_summary["最高得点"]}点',
        f'{class_summary["最低得点"]}点',
    )