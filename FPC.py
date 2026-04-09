
from functools import reduce


nums = [1, 2, 3, 4]
numb = 5
result = reduce(lambda a, b: a / b, nums, numb)
print(result)