"""
[파이썬 기본 문법 - 리스트와 딕셔너리 활용]

문제 설명:
- 학생들의 이름과 점수를 입력받아 평균 점수 이상인 학생들을 찾아 출력합니다.
- 파이썬의 기본 자료구조인 리스트와 딕셔너리를 활용하는 문제입니다.

입력:
- students: 학생 정보를 담은 딕셔너리 리스트
  예: [{"name": "Alice", "score": 85}, {"name": "Bob", "score": 92}]

출력:
- 평균 점수
- 평균 이상인 학생들의 이름 리스트

예제:
입력:
[
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 95}
]

출력:
평균 점수: 87.5
평균 이상 학생: ['Bob', 'David']
"""

def avg(n):
    return sum(x["score"] for x in n) / len(n)


def find_above_average_students(students):
    average = avg(students)
    above_average_students = [x["name"] for x in students if x["score"] > average]
    
    return average, above_average_students

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    students1 = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78},
        {"name": "David", "score": 95}
    ]
    
    avg2, students = find_above_average_students(students1)
    print(f"평균 점수: {avg2}")
    print(f"평균 이상 학생: {students}")
    print()
    
    # 테스트 케이스 2
    students2 = [
        {"name": "Emma", "score": 70},
        {"name": "Frank", "score": 85},
        {"name": "Grace", "score": 90}
    ]
    
    avg2, students = find_above_average_students(students2)
    print(f"평균 점수: {avg2}")
    print(f"평균 이상 학생: {students}")


