"""
RECORD CHECK  -  my version
===========================

Name  : ASHIRA BIBI AWOODUN
Lane  :  AI 
Date  : 06 november 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== 

def parse_line(raw_line): #create a function to clean the record 
    """Turn a messy survey record into a dict with label, rating and age"""
    line = raw_line.strip() #removes all empty spaces in front & end of rawline
    label_part , rest = line.split(",", 1) #split the first comma, the rest stays together (rating & age)

    label = label_part.strip().lower() #write label in lowercase + remove spaces before and after the comma
    pieces = rest.split(",") #now work with rest, and split them into 2 different; rating , age

    #create a dict
    result = {"label" : label}

    for piece in pieces: #now work with rating & age
        key, value = piece.split ("=") #make rating be the key and 4 be the value, for the dict

        #strip both separately - remove any spaces + convert value into float 
        key = key.strip().lower()
        value = float(value.strip())

        #in the dict created called result, store the value(age) in the section labelled key(rating)
        result[key] = value 
    return result


def status_of (rating, age):
    """Determine whether the age is less than or equal to the rating."""
    if age <= rating: 
        return "FLAGGED"

    else:
        return "OK"
    



with open ("miniproject_file.txt") as f: #opening file, read all lines at once into a list called raw_records
    raw_records = f.readlines()   #the set of lines in the files are now called raw_records


flagged_record_count = 0


for raw_record in raw_records: #in raw_records, go through each line
    try:
        data = parse_line(raw_record) #the cleaned lines are now kept in a dict called data
        status = status_of (data["rating"], data["age"]) #call status_of from dict data
        print (data, status)
    
        if status == "FLAGGED":
            flagged_record_count +=1 
    except ValueError: #this has been added because in file, string "Rating=high" can't be converted to float
            print ("Could not parse line :", raw_record)

print ("There was a total of", len(raw_records), "records", "and", flagged_record_count, "were flagged.") 
#len(raw_records) determines total amount of records in the file/dict.


