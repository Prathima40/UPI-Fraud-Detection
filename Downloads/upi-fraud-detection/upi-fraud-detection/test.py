import pandas as pd

df = pd.read_csv("onlinefraud.csv")
df.sample(5000).to_csv("test.csv", index=False)

print("Test file created!")