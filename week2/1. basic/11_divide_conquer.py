"""
[분할 정복 - 배열의 최댓값 찾기]

문제 설명:
- 분할 정복(Divide and Conquer) 방식으로 배열의 최댓값을 찾습니다.
- 배열을 반으로 나누고, 각 부분의 최댓값을 구한 후 비교합니다.

입력:
- arr: 정수 배열
- left: 시작 인덱스
- right: 끝 인덱스

출력:
- 배열의 최댓값

예제:
입력: [3, 5, 1, 8, 2, 9, 4]
출력: 9

"""

def find_max_divide_conquer(arr, left, right):
    def mergeSort(arr: list):
        if len(arr) <= 1:
            return arr

        mid: int = len(arr) // 2
        left: list = arr[:mid]
        right: list = arr[mid:]

        return merge(mergeSort(left), mergeSort(right))

    def merge(left:list, right:list):
        result:list = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])

        return result
    result1 = mergeSort(arr)
    return result1[len(result1)-1]
    

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [3, 5, 1, 8, 2, 9, 4]
    result1 = find_max_divide_conquer(arr1, 0, len(arr1) - 1)
    print(f"배열: {arr1}")
    print(f"최댓값: {result1}")
    print()
    
    # 테스트 케이스 2
    arr2 = [10, 20, 30, 40, 50]
    result2 = find_max_divide_conquer(arr2, 0, len(arr2) - 1)
    print(f"배열: {arr2}")
    print(f"최댓값: {result2}")
    print()
    
    # 테스트 케이스 3
    arr3 = [100]
    result3 = find_max_divide_conquer(arr3, 0, len(arr3) - 1)
    print(f"배열: {arr3}")
    print(f"최댓값: {result3}")

