"""
RECORD CHECK  -  my version
===========================

Name  : ASHIRA AWOODUN
Lane  :  AI 
Date  : 24 October 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS


class Record:
    def __init__ (self, label, value,limit):
        "store label, value, limit for one record"""
        self.label = label
        self.value = value
        self.limit = limit

    def status (self):
        """returns the status of percentage of self.value over self.limit"""
        p = (self.value / self.limit)*100

        if p >= 100:
            return "OVER LIMIT"

        elif p>= 90:
            return "WARNING"

        else:
            return "OK"


# ==================================================================== RECORDS

def load_records(path):
    """Read label, value, limit from a file and return record"""
    records = []
    with open (path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            value = float (value)
            limit = float (limit)
            records.append(Record(label, value, limit))

    return records

loaded = load_records("records_miniproject.txt")

# ==================================================================== OUTPUT

over_limitcount = 0 

for record in loaded:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print (f"Value : {record.value}")
    print (f"Limit : {record.limit}")
    print (f"Status : {record.status()}")

    

    print("=" * 34)

    if record.status() == "OVER LIMIT":
        over_limitcount += 1 

print ()

print(f"TOTAL OVER LIMIT COUNT: {over_limitcount}") 


# ==========================================================================
