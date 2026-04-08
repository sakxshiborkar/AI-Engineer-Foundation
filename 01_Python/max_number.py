def find_max(numbers):
    max_num = numbers[0]  # assume first element is max

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num


# Example usage
nums = [3, 7, 2, 9, 5]
result = find_max(nums)

print("Maximum number is:", result)