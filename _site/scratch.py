# def pair_with_targetsum(arr, target_sum):
#   nums = {}  # to store numbers and their indices
#   print("nums:", nums)
#   for i, num in enumerate(arr):
    
#     if target_sum - num in nums:
#       print("now nums:", nums)
#       return [nums[target_sum - num], i]
#     else:
#       nums[arr[i]] = i
#   return [-1, -1]


# def main():
#   print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
#   print(pair_with_targetsum([2, 5, 9, 11], 11))


# main()

s1 = 'geek'

# changing start index to 2 from 0
print(list(enumerate(s1, 4)))

for x in list(enumerate(s1)):
    print(x[0], x[1])