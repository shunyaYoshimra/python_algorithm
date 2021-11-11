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
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = temp
    return numbers


def bucket_sort(numbers: List[int]):
    max_num = max(numbers)
    nums_length = len(numbers)
    size = max_num // nums_length

    buckets = [[] for _ in range(size)]
    for num in numbers:
        i = num // size
        if i != size:
            buckets[i].append(num)
        else:
            buckets[size-1].append(num)

    for i in range(size):
        insertion_sort(buckets[i])

    result = []
    for i in range(size):
        result += buckets[i]

    return result


if __name__ == "__main__":
    nums = getNums
    print(bucket_sort(nums))
