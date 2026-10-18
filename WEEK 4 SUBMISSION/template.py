"""
RECORD CHECK  -  my version
===========================

Name  : Ashira B Awoodun
Lane  :  AI 
Date  : 16 October 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
#done up to threshold and typical only


def load_records(path):
    """Taking the records from the file"""
    records = []
    try: 
        with open(path) as f:
            for line in f:
                label, value, limit = line.strip().split(",")
                record =  {"label": label, "value": float(value), "limit": float(limit)}
    
                records.append(record) #in the records list, add the record dict
    except FileNotFoundError:
        print ("File cannot be found")
    
    return records

def check_record (value, limit):
    """Return difference and percent using value and limit"""
    difference = value - limit 
    percent = (value/limit) * 100
    return difference, percent

def print_report (label, value, limit, difference,percent, status):
    """print record for one report at a time"""
    print ()
    print ("=" *34)
    print (f"RECORD CHECK -  {label}")
    print ("=" * 34)

    print (f"Rows Loaded   : {value:>10.2f}")
    print (f"Rows Expected : {limit:>10.2f}")
    print (f"Difference    : {difference:>10.2f}")
    print (f"Percent       : {percent:>10.2f} %")
    print (f"Status        : {status:>10}")

overlimit_count = 0 

records = load_records("my_records.txt")

for record in records:
    difference, percent = check_record(record["value"], record["limit"])
    if percent >= 100:
        status = "OVER LIMIT"
        overlimit_count += 1

    elif percent>= 90:
        status = "WARNING"

    else:
        status = "OK"

    
    print_report (record["label"], record["value"], record["limit"], difference,percent, status)

print (f"RECORDS OVER LIMIT : {overlimit_count}")
