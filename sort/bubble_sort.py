from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
  len_numbers = len(numbers)
  for i in range(len_numbers-1):
    for j in range(len_numbers-i-1):
      if numbers[j] >= numbers[j+1]:
        numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
  return numbers


if __name__ == '__main__':
  nums = [1,7,19,3,4,6,9,17]
  print(bubble_sort(nums))