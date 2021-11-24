from typing import List


def getNums() -> List[int]:
    str_list = [s for s in input().split()]
    nums = list(map(int, str_list))
    return nums


def selection_sort(numbers: List[int]) -> List[int]:
    nums_length = len(numbers)
    for i in range(nums_length-1):
        temp_id = i
        for j in range(i+1, nums_length):
            if numbers[temp_id] > numbers[j]:
                temp_id = j
        numbers[i], numbers[temp_id] = numbers[temp_id], numbers[i]

    return numbers


if __name__ == "__main__":
    nums = getNums()
    print(selection_sort(nums))
