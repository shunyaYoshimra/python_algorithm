from typing import List


def getNums() -> List[int]:
    str_list = [s for s in input().split()]
    nums = list(map(int, str_list))
    return nums


def comb_sort(numbers: List[int]) -> List[int]:
    nums_length = len(numbers)
    gap = nums_length
    swapped = True

    while gap != 1 or swapped:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1

        swapped = False

        for i in range(0, nums_length - gap):
            if numbers[i] > numbers[i + gap]:
                numbers[i], numbers[i+gap] = numbers[i+gap], numbers[i]
                swapped = True
    return numbers


if __name__ == "__main__":
    nums = getNums()
    print(comb_sort(nums))
