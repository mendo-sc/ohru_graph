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

plt.style.use('ggplot')

dates, unemp_rates = [], []
for row in reader:
    current_date = datetime.strptime(row[0], '%Y-%m-%d')
    rate = float(row[1])
    dates.append(current_date)
    unemp_rates.append(rate)

fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(dates, unemp_rates, color='blue', linewidth=2)

ax.set_title("Ohio Unemployment (by Month): 1976 - 2022", fontsize=24)
ax.set_xlabel("Date", fontsize=20)
ax.set_ylabel("Unemp Rate", fontsize=20)
ax.tick_params(labelsize=18)

plt.show()