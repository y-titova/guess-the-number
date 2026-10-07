import random
import csv


def sequential_search(target, min_number, max_number):
    attempts = 0

    for number in range(min_number, max_number + 1):
        attempts += 1

        if number == target:
            return attempts
        

def binary_search(target, min_number, max_number):
    attempts = 0
    left = min_number
    right = max_number

    while left <= right:
        attempts += 1
        middle = (left + right) // 2

        if middle == target:
            return attempts
        elif middle < target:
            left = middle + 1
        else:
            right = middle - 1


def random_search(target, min_number, max_number):
    attempts = 0
    available_numbers = list(range(min_number, max_number + 1))

    while True:
        number = random.choice(available_numbers)
        available_numbers.remove(number)
        attempts += 1

        if number == target:
            return attempts
        

def run_experiment(number_of_trials, min_number, max_number):
    sequential_results = []
    random_results = []
    binary_results = []

    for _ in range(number_of_trials):
        target = random.randint(min_number, max_number)

        sequential_results.append(
            sequential_search(target, min_number, max_number)
        )

        random_results.append(
            random_search(target, min_number, max_number)
        )

        binary_results.append(
            binary_search(target, min_number, max_number)
        )

    return sequential_results, random_results, binary_results


def get_statistics(results):
    return {
        "average": sum(results) / len(results),
        "minimum": min(results),
        "maximum": max(results),
    }


def save_results(filename, results):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Диапазон",
            "Метод",
            "Среднее",
            "Минимум",
            "Максимум"
        ])

        for result in results:
            writer.writerow(result)


sequential_results_100, random_results_100, binary_results_100 = run_experiment(
    1000, 1, 100
)

sequential_results_1000, random_results_1000, binary_results_1000 = run_experiment(
    1000, 1, 1000
)


stats_sequential_100 = get_statistics(sequential_results_100)
stats_random_100 = get_statistics(random_results_100)
stats_binary_100 = get_statistics(binary_results_100)

stats_sequential_1000 = get_statistics(sequential_results_1000)
stats_random_1000 = get_statistics(random_results_1000)
stats_binary_1000 = get_statistics(binary_results_1000)

results = [
    [
        "1-100",
        "Последовательный поиск",
        stats_sequential_100["average"],
        stats_sequential_100["minimum"],
        stats_sequential_100["maximum"]
    ],
    [
        "1-100",
        "Случайный поиск",
        stats_random_100["average"],
        stats_random_100["minimum"],
        stats_random_100["maximum"]
    ],
    [
        "1-100",
        "Бинарный поиск",
        stats_binary_100["average"],
        stats_binary_100["minimum"],
        stats_binary_100["maximum"]
    ],
    [
        "1-1000",
        "Последовательный поиск",
        stats_sequential_1000["average"],
        stats_sequential_1000["minimum"],
        stats_sequential_1000["maximum"]
    ],
    [
        "1-1000",
        "Случайный поиск",
        stats_random_1000["average"],
        stats_random_1000["minimum"],
        stats_random_1000["maximum"]
    ],
    [
        "1-1000",
        "Бинарный поиск",
        stats_binary_1000["average"],
        stats_binary_1000["minimum"],
        stats_binary_1000["maximum"]
    ]
]

save_results("results/results.csv", results)