import pandas as pd
from midas_quant.feed import PandasFeeder, PandasPart

"""
Test function for the PandasFeeder class.
"""
# Create sample DataFrames
df1 = pd.DataFrame({
    'A': range(10),
    'B': range(10, 20)
})

df2 = pd.DataFrame({
    'A': range(20, 30),
    'B': range(30, 40)
})

# Initialize PandasFeeder with the list of DataFrames
feeder = PandasFeeder(
    dfs=[df1, df2], 
    window=3, 
    backword=True, 
    part_class=PandasPart
)

# Display total number of segments
print(f"Total segments: {len(feeder)}\n")

# Iterate over the feeder using a for loop
print("Iterating over PandasFeeder:")
for idx, (part, is_change) in enumerate(feeder):
    print(f"Segment {idx + 1}:")
    print(part)
    print(f"DataFrame Changed: {is_change}")
    print("-" * 40)

# Reset the feeder
feeder.reset()
print("\nAfter resetting the feeder:")

# Using the next method to iterate
print("Iterating using the next() method:")
while True:
    part, change = feeder.next()
    if part is None and change is None:
        break
    print(f"Next Segment:")
    print(part)
    print(f"DataFrame Changed: {change}")
    print("-" * 40)