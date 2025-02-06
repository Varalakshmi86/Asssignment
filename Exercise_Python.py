import csv
import math

with open("/home/nineleaps/PYTHON_DATA/sales_24.csv", mode="r", newline="") as infile:
    reader = csv.reader(infile)

    header = next(reader)

    with open("/home/nineleaps/PYTHON_DATA/sales_24.csv", mode="w", newline="") as outfile:
        writer = csv.writer(outfile)

        writer.writerow(header)

        for row in reader:
            try:

                amount_index = header.index("Amount")

                if row[amount_index] != "":
                    row[amount_index] = str(math.floor(float(row[amount_index])))

                writer.writerow(row)
            except ValueError:

                writer.writerow(row)
