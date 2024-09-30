import numpy as np
from midas_quant.feed import *

import pandas as pd

# Sample DataFrame
data = {
    'A': [10, 20, 30, 40, 50],
    'B': [15, 19, 35, 45, 55]
}
df = pd.DataFrame(data)

# Initialize PandasPart
pandas_part = PandasPart(df, backword=False)

# Access a single row
row = pandas_part[2]
print(f"The value at the 2th index when calculated forward : {row.A}, {row.B} ")
assert row.A == 30 and row.B == 35

# Access a slice of rows
rows = pandas_part[1:3]
print(f"pandas_part[1:3] forward...\n{rows}")
assert rows[0].A == 20 and rows[0].B == 19

# Compare values
is_up = pandas_part.upCompare(2, 'A', 'B')
print(f"A > B at index 2: {is_up}")
assert is_up == False

is_up = pandas_part.upCompare(1, 'A', 'B')
print(f"A > B at index 1: {is_up}")
assert is_up == True

# Check cross event
has_crossed = pandas_part.cross(3, 'A', 'B', updn="up")
print(f"Crossed up at index 3: {has_crossed}")
assert has_crossed == False

has_crossed = pandas_part.cross(2, 'A', 'B', updn="down")
print(f"Crossed up at index 2: {has_crossed}")
assert has_crossed == True

pandas_part = PandasPart(df, backword=True)
# Access a slice of rows
rows = pandas_part[0:3]
print(f"pandas_part[0:3] backword...\n{rows}")
assert rows[0].A == 50 and rows[0].B == 55
