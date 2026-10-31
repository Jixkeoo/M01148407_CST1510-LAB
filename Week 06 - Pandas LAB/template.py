"""
RECORD CHECK  -  my version
===========================

Name  :  Leon Beaupere
Lane  :  Cyber
Date  :  31/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("my_record.csv")

df["percent"] = (df["value"] / df["limit"]) *100
df["status"] = df["percent"].apply(lambda p: "OvER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK"))

print(df)
print(df[df["status"] != "OK"])
print(df.groupby("status").size())

df.to_csv("my_record_report.csv", index=False)

df["status"].value_counts().plot(kind="bar")
plt.savefig("status_counts.png")