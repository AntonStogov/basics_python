odd_nums = [num for num in range(1, int(input('n: ')) + 1) if num % 2 != 0]
print(*odd_nums, sep=', ')