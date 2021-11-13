from typing import List


def getNums() -> List[int]:
    str_list = [s for s in input().split()]
    nums = list(map(int, str_list))
    return nums


def insertion_sort(numbers: List[int]) -> List[int]:
    nums_length = len(numbers)
    for i in range(1, nums_length):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and temp < numbers[j]:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = temp
    return numbers


if __name__ == "__main__":
    nums = getNums()
    print(insertion_sort(nums))
