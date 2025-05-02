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