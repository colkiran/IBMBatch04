
import csv
from prettytable import PrettyTable

with open("Employee.csv", "r") as CSVR:
    emp_detials = csv.reader(CSVR)
    prtyTbl = PrettyTable(next(emp_detials))

    for row in emp_detials:
        prtyTbl.add_row(row)

print(prtyTbl)


    # colnames = next(emp_detials)
    # print(*colnames)

    # for rec in emp_detials:
    #     print(*rec)

