"""
RECORD CHECK  -  my version
===========================

Name  :ASHIRA B AWOODUN
Lane  :  AI 
Date  : 09.10.2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



# your function(s) go here
def status_of (percent):
    """return percent with labels of overlimit, warning or ok if they fit the if condition"""
    if percent >= 100:
        return "OVER LIMIT"

    elif percent >= 90:
        return "WARNING"

    else:
        return "OK"

def check (value, limit):
    """Return difference and percent using value and limit"""
    difference = value - limit 
    percent = (value/limit) * 100
    return difference, percent
    
def print_report (label, value, limit, difference,percent, status):
    """print the values asked for, count the number of times there was overlimit"""
    print ()
    print ("=" *34)
    print (f"RECORD CHECK -  {label}")
    print ("=" * 34)

    print (f"Rows Loaded   : {value:>10.2f}")
    print (f" Rows Expected : {limit:>10.2f}")
    print (f" Difference    : {difference:>10.2f}")
    print (f" Percent       : {percent:>10.2f} %")
    print (f" status        : {status:>10}")


overlimit_count = 0


while True:

    label = input ("Enter label: ( or quit) ")
    if label == "quit":
        break

    value = float(input ("Enter rows loaded:  "))
    limit = float(input("Enter rows expected:  "))



    difference, percent = check (value, limit)
    status = status_of (percent)

    if status == "OVER LIMIT":
        overlimit_count +=1 


#need to close the definition
    print_report (label, value, limit, difference,percent, status)

print (f"Records Over Limit : {overlimit_count}")

print ("="*34)


