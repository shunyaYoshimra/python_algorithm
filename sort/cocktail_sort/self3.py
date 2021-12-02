from typing import List


def getNums() -> List[int]:
    str_list = [s for s in input().split()]
    nums = list(map(int, str_list))
    return nums


def cocktail_sort(numbers: List[int]) -> List[int]:
    nums_length = len(numbers)
    start = 0
    end = nums_length
    swapped = True
    while swapped:
        swapped = False
        for i in range(start, end-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True
        if not swapped:
            break
        end -= 1

        for i in range(end-1, start-1, -1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True
        start += 1
    return numbers


if __name__ == '__main__':
    nums = getNums()
    print(cocktail_sort(nums))
