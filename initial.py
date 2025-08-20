def calculate_average(numbers):
    number_count = len(numbers)
    if number_count == 0:
        return 0
    total_sum = sum(numbers)
    average = total_sum / number_count
    return average
