"""
RECORD CHECK  -  my version
===========================

Name  : Ashira Bibi Awoodun
Lane  :  AI 
Date  : 30 September 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

dataset_name= input ("enter dataset name")
rows_loaded = int(input ("enter rows loaded"))
rows_expected = int(input("enter rows expected"))

print ("="*34)
print ("dataset name - ", dataset_name)
print("="* 34)

print(f"{'rows_loaded' :<15} = {rows_loaded:>15.2f}")
print(f"{'rows_expected' :<15} = {rows_expected:>15.2f}")

difference = rows_expected - rows_loaded 
print(f"{'Difference' :<15} = {difference:>+15.2f}")
percent = rows_loaded / rows_expected * 100
print(f"{'Percent' :<15} = {percent:>15.2f} %")

percent_missing = difference/ rows_expected *100
print(f"{'Percent missing':<15} = {percent_missing:>15.2f} %")
print ("Percent missing is used to calculate the percentage of rows missing over the total expected rows")

print("=" * 34)


