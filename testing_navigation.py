import csv
csv1 = csv.reader(open("tickers1.csv","r"))
csv2 = csv.reader(open("Final.csv","r"))
while True:
    try:
        line1 = next(csv1)
        line2 = next(csv2)
        if line1 not in line2:
            print("Not")
        else:
            print("Equal")
    except StopIteration:
        break
True