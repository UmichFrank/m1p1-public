import os
import pandas as pd


def create_file_if_not_exists(filename):

    if not os.path.exists(filename):

        with open(filename, "w", encoding="utf-8"):
            pass


def write_to_file(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data)


def append_to_file(filename, data_to_add):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(data_to_add)


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def count_lines_in_file(filename):

    with open(filename, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def get_longest_line(filename):

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        return max(lines, key=lambda s: len(s.rstrip("\n"))).rstrip("\n") if lines else ""


def add_column_to_csv(filename, columnName, columnValues):
    df = pd.read_csv(filename)
    if len(columnValues) != len(df):
        raise ValueError("Length of columnValues must match number of rows in CSV")
    df[columnName] = columnValues
    df.to_csv(filename, index=False)


def get_avg_age(filename):
    df = pd.read_csv(filename)
    return float(df["Age"].mean())


def get_profession_count(filename):
    df = pd.read_csv(filename)
    return df["Profession"].value_counts()


if __name__ == "__main__":
    filename = "testfile.csv"
    create_file_if_not_exists(filename)

    write_to_file(filename, "Name,Age\nAlice,25\nBob,30\n")
    append_to_file(filename, "Charlie,35\nDaisy,40\nEve,28\nFrank,31\n")

    print("Content of file:\n" + read_file(filename))
    totalLines = count_lines_in_file(filename)
    print(f"Total lines: {totalLines}")

    longestLine = get_longest_line(filename)
    print("Longest line:", longestLine)

    professions = ["Engineer", "Doctor", "Lawyer", "Chef", "Artist", "Engineer"]
    add_column_to_csv(filename, "Profession", professions)

    print(read_file(filename))

    averageAge = get_avg_age(filename)
    print(f"Average Age: {averageAge}")

    professionCount = get_profession_count(filename)
    print("Profession counts:\n", professionCount)

    append_to_file(filename, "\nGinny,29,Doctor")

    updated_df = pd.read_csv(filename)
    updated_df = updated_df[updated_df["Age"] > 30]
    print("People older than 30:\n", updated_df)

    group_by_profession = updated_df.groupby("Profession")["Age"].mean()
    print("Average age per profession for people older than 30:\n", group_by_profession)