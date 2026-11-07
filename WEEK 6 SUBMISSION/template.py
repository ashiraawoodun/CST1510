"""
RECORD CHECK  -  my version
===========================

Name  : Ashira Awoodun
Lane  :  AI    
Date  : 27 October 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

try:
    df = pd.read_csv("my_file.csv")
except FileNotFoundError:
    print ("File not found. Make sure file is in the folder")
    exit()


df["percent"] = ((df["value"]/df["limit"])*100).round(2)

df["status"] = df["percent"].apply(lambda p: "OVER LIMIT" if p>=100 else ("WARNING" if p>=90 else "OK"))

print ("FULL DATAFRAME")
print (df)

#from dataframe, select status that is NOT OK
print ("\nDATAFRAME showing only the rows that are not 'OK'")
rows_not_ok = df[df["status"] != "OK"]
print(rows_not_ok)

#how many different status counts are there?
print ("\nCount per status")
status_counts = df.groupby("status")["label"].agg("count")
print (status_counts)

#saving to mini project file
df.to_csv("mini_project_W6.csv", index= False)

#creating bar chart and saving it 
import matplotlib.pyplot as plt
df ["status"].value_counts().plot(kind="bar", rot= 0) #makes labels in x axis horizontal

plt.title("status counts")
plt.xlabel("Status")
plt.ylabel("Number of counts")
plt.tight_layout() #to fix the layout of the image
plt.savefig("W6_status_counts.png")
plt.show()


