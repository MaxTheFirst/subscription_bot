from datetime import datetime

n = datetime(23, 8, 27, 21, 5, 1)
x = datetime(n.year, n.month, n.day+1)
delta = (x-n).seconds//3600
print(delta)