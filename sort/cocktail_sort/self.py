from typing import List


def getNums() -> List[int]:
    str_list = [s for s in input().split()]
    nums = list(map(int, str_list))
    return nums


def cocktail_sort(numbers: List[int]) -> List[int]:
    num_length = len(numbers)
    start = 0
    end = num_length - 1
    swapped = True

    while swapped:
        swapped = False
        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

            if not swapped:
                break

            end -= 1
            swapped = False

        for i in range(end-1, start-1, -1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

    return numbers


if __name__ == "__main__":
    nums = getNums()
    print(cocktail_sort(nums))
