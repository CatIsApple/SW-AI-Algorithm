import sys
sys.setrecursionlimit(10**6)
"""
[복잡도 분석 - Big O, 시간 복잡도, 공간 복잡도]

문제 설명:
- 여러 알고리즘의 시간 복잡도와 공간 복잡도를 이해하고 비교합니다.
- 동일한 문제를 다른 복잡도로 해결하는 방법을 학습합니다.
- 배열에서 중복 원소를 찾는 문제를 여러 방법으로 구현합니다.

입력:
- nums: 정수 배열

출력:
- 중복된 원소들의 리스트

예제:
입력: [4, 3, 2, 7, 8, 2, 3, 1]
출력: [2, 3]
"""


def find_duplicates_brute_force(nums):

    duplicates = []
    n = len(nums)

    def brute_force(i):
        if i >= n:
            return

        for idx in range(i + 1, n):
            if nums[i] == nums[idx]:
                if nums[i] not in duplicates:
                    duplicates.append(nums[i])

        brute_force(i+1)

    brute_force(0)

    return duplicates


def find_duplicates_sorting(nums):

    if not nums:
        return []

    duplicates = set()

    seen = set()

    def find_Dup(n):
        # n = 0 len(nums) = 1000
        if n >= len(nums):
            return 0
        else:
            if nums[n] in seen:
                duplicates.add(nums[n])
            else:
                seen.add(nums[n])
        return find_Dup(n + 1)
    find_Dup(0)

    return list(duplicates)


def find_duplicates_hash(nums):
    digitCount = len(str(max(nums)))

    numList = [[[] for _ in range(10)] for _ in range(digitCount)]
    result = []
    duplicates = set()
    seen = set()

    for n in range(digitCount):

        for i in nums:
            strNum = str(i).zfill(digitCount)  # 3자리 무조건 채우기
            strLastNum = strNum[len(strNum) - 1 - n]
            numList[n][int(strLastNum)].append(strNum)
        result = []
        for i in numList[n]:
            result.extend(i)

    def find_Dup(n):
        if n >= len(result):
            return 0
        else:
            if result[n] in seen:
                duplicates.add(int(result[n]))
            else:
                seen.add(result[n])
        return find_Dup(n + 1)
    find_Dup(0)

    # 답
    return list(duplicates)


def measure_time(func, nums, method_name):
    """실행 시간 측정 헬퍼 함수"""
    result = func(nums[:])
    print(f"{method_name}: {sorted(result)}")
    print()


if __name__ == "__main__":

    print("=== 테스트 케이스 1: 작은 배열 ===")
    nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
    print(f"입력: {nums1}\n")

    result1 = find_duplicates_brute_force(nums1)
    print(f"방법1 (Brute Force): {sorted(result1)}")

    result2 = find_duplicates_sorting(nums1)
    print(f"방법2 (Sorting): {sorted(result2)}")

    result3 = find_duplicates_hash(nums1)
    print(f"방법3 (Hash): {sorted(result3)}")
    print()

    print("=== 테스트 케이스 2: 성능 비교 (n=1000) ===")
    import random
    random.seed(42)  # 동일한 결과를 위한 시드 설정
    nums2 = [random.randint(1, 500) for _ in range(1000)]

    measure_time(find_duplicates_brute_force, nums2, "방법1 (O(n²))")
    measure_time(find_duplicates_sorting, nums2, "방법2 (O(n log n))")
    measure_time(find_duplicates_hash, nums2, "방법3 (O(n))")

    print("=== 복잡도 분석 요약 ===")
    print("방법1 - Brute Force:")
    print("  시간: O(n²), 공간: O(k)")
    print("  특징: 간단하지만 느림")
    print()
    print("방법2 - Sorting:")
    print("  시간: O(n log n), 공간: O(1)")
    print("  특징: 추가 메모리 없이 효율적")
    print()
    print("방법3 - Hash:")
    print("  시간: O(n), 공간: O(n)")
    print("  특징: 가장 빠르지만 메모리 사용")
