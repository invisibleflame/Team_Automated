import csv
import datetime

with open('log.csv', 'a+', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["dfg", datetime.datetime.now()])