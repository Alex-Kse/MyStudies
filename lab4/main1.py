# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME,"r") as f:
        data1 = csv.DictReader(f)
        data2 = []
        lines = [line for line in data1]
        for line in lines:
            data2.append(line)



    with open(OUTPUT_FILENAME,"w") as r:
        r.write(json.dumps (data2, indent=4))


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
          print(line, end="")