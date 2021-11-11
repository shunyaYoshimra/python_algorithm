import random
from typing import List


def getNums() -> List[int]:
    str_list = [s for s in input().split()]
    nums = list(map(int, str_list))


def in_order(numbers: List[int]) -> List[int]:
    nums_length = len(numbers)
    for i in range(nums_length-1):
        if numbers[i] > numbers[i+1]:
            return False

    return True


def bogo_sort(numbers: List[int]) -> List[int]:
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers


if __name__ == "__main__":
    nums = getNums()
    print(bogo_sort(nums))
