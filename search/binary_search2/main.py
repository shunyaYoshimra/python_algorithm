# binary search
from typing import List


def getNums() -> List[int]:
    str_list = [s for s in input().split()]
    nums = list(map(int, str_list))
    return nums


def binary_search(nums: List[int], target: int) -> int:
    def _binary_search(nums: List[int], target: int, min: int, max: int) -> int:
        if min > max:
            return -1
        center = (min + max) // 2
        if nums[center] == target:
            return center
        elif nums[center] < target:
            return _binary_search(nums, target, center + 1, max)
        else:
            return _binary_search(nums, target, min, max - 1)

    return _binary_search(nums, target, 0, len(nums) - 1)


if __name__ == "__main__":
    nums = getNums()
    print(binary_search(nums, 100))
