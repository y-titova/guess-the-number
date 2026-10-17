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



def create_combined_chart(results, filename):
    ranges = ["1-100", "1-1000"]
    methods = [
        "Последовательный поиск",
        "Случайный поиск",
        "Бинарный поиск"
    ]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    for ax, number_range in zip(axes, ranges):
        averages = []

        for method in methods:
            for row in results:
                if (
                    row["Диапазон"] == number_range
                    and row["Метод"] == method
                ):
                    averages.append(float(row["Среднее"]))

        ax.bar(["Последовательный", "Случайный", "Бинарный"], averages)
        ax.set_title(f"Диапазон {number_range}")
        ax.set_ylabel("Среднее количество попыток")

    fig.suptitle("Сравнение способов поиска")
    fig.tight_layout()
    fig.savefig(filename)
    plt.close(fig)

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

create_combined_chart(
    results,
    "results/chart_comparison.png"
)

print("Графики созданы.")
