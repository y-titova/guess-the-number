import csv

import matplotlib.pyplot as plt


def read_results(filename):
    results = []

    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            results.append(row)

    return results


def create_chart(results, number_range, filename):
    methods = []
    averages = []

    for row in results:
        if row["Диапазон"] == number_range:
            methods.append(row["Метод"])
            averages.append(float(row["Среднее"]))

    plt.figure(figsize=(8, 5))

    plt.bar(methods, averages)

    plt.title(f"Среднее количество попыток: диапазон {number_range}")
    plt.ylabel("Количество попыток")
    plt.xticks(rotation=15)

    plt.tight_layout()
    plt.savefig(filename)

    plt.close()


results = read_results("results/results.csv")

create_chart(
    results,
    "1-100",
    "results/chart_100.png"
)

create_chart(
    results,
    "1-1000",
    "results/chart_1000.png"
)

print("Графики созданы.")