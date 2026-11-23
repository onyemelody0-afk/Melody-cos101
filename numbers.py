
def get_number_list():
    user_input = input("Enter numbers separated by spaces: ")
    parts = user_input.split()
    numbers = []
    for item in parts:
        numbers.append(float(item))
    return numbers


def sum_list(numbers):
    total = sum(numbers)
    return total


def mean_list(numbers):
    mean = sum(numbers) / len(numbers)
    return mean


def median_and_mode(numbers):
    sorted_numbers = sorted(numbers)
    mid = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 0:
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        median = sorted_numbers[mid]

    mode = max(numbers, key=numbers.count)
    return median, mode

my_numbers = get_number_list()

total_sum = sum_list(my_numbers)
average = mean_list(my_numbers)
median, mode = median_and_mode(my_numbers)

print("Sum:", total_sum)
print("Mean:", average)
print("Median:", median)
print("Mode:", mode)
