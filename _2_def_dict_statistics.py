from pprint import pprint

def get_statistics(numbers):
    sum_number = sum(numbers)
    avg_number = sum(numbers) / len(numbers)
    min_number = min(numbers)
    max_number = max(numbers)
    length_number = len(numbers)
    return {
        "sum": sum_number,
        "avg": avg_number,
        "min": min_number,
        "max": max_number,
        "length": length_number,
    }

nums = [4, 8, 2, 10, 6]

pprint(get_statistics(nums), width=1)