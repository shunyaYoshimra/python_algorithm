# バブルソート

from typing import List


def getNums() -> List[int]:
    str_list = [s for s in input().split()]
    nums = list(map(int, str_list))
    return nums


def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers-1):
        for j in range(len_numbers-i-1):
            if numbers[j] >= numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


if __name__ == '__main__':
    nums = getNums()
    print(bubble_sort(nums))
