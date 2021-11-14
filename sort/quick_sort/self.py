from typing import List


def getNums() -> List[int]:
    str_list = [s for s in input().split()]
    nums = list(map(int, str_list))
    return nums


def partitions(numbers: List[int], low: int, high: int) -> int:
    pivot = numbers[high]
    i = low - 1
    for j in range(low, high):
        if numbers[j] < pivot:
            i += 1
            numbers[j], numbers[i] = numbers[i], numbers[j]
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i+1


def quick_sort(numbers: List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partitions(numbers, low, high)
            _quick_sort(numbers, low, partition_index-1)
            _quick_sort(numbers, partition_index+1, high)
    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers


if __name__ == "__main__":
    nums = getNums()
    print(quick_sort(nums))
