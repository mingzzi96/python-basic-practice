def count_common_elements(list1, list2):
    # 두 리스트에서 공통된 요소를 찾기 위해 집합(set)을 사용합니다.
    set1 = set(list1)
    set2 = set(list2)
    
    # 두 집합의 교집합을 구하고 그 길이를 반환합니다.
    common_elements = set1.intersection(set2)
    return len(common_elements)

# 예시 리스트
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# 공통된 요소의 개수를 출력합니다.
print("두 리스트의 공통된 요소 개수:", count_common_elements(list1, list2))
