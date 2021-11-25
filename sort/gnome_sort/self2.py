from typing import List


def getNums() -> List[int]:
    str_list = [s for s in input().split()]
    nums = list(map(int, str_list))
    return nums


def gnome_sort(numbers: List[int]) -> List[int]:
    nums_length = len(numbers)
    index = 1

    while index < nums_length:
        if index == 0:
            index = 1
        if numbers[index] >= numbers[index-1]:
            index += 1
        else:
            numbers[index], numbers[index-1] = numbers[index-1], numbers[index]
            index -= 1
    return numbers


if __name__ == '__main__':
    nums = getNums()
    print(gnome_sort(nums))
