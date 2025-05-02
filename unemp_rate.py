from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('data/OHUR.csv')
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# Header information
for index, column_head in enumerate(header_row):
    print(index, column_head)

dates, unemp_rates = [], []
for row in reader:
    current_date = datetime.strptime(row[0], '%Y-%m-%d')
    rate = float(row[1])
    dates.append(current_date)
    unemp_rates.append(rate)

fig, ax = plt.subplots()
ax.plot(dates, unemp_rates)
plt.show()