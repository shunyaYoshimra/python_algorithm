# binary search
from typing import List


def getNums() -> List[int]:
    str_list = [s for s in input().split()]
    nums = list(map(int, str_list))
    return nums


def binary_search(nums: List[int], target: int) -> int:
    min, max = 0, len(nums) - 1
    while min <= max:
        center = (min + max) // 2
        if nums[center] == target:
            return center
        elif nums[center] < target:
            min = center + 1
        else:
            max = center - 1


if __name__ == "__main__":
    nums = getNums()
    print(binary_search(nums, 100))
