"""
RECORD CHECK  -  my version
===========================

Name  : Ashira Awoodun
Lane  :  AI 
Date  : 03 October 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""





#how many are over limit at start? 0 are over limit 

over_limit_count = 0
#i need to input a label

label = input("Enter label or 'quit' to stop")


#when label = quit, the code will stop, when it is NOT EQUAL TO QUIT, IT WILL CONTINUE
while label != "quit" :

    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}") #label becomes my dataset name hence i erase dataset name
    print("=" * 34)

    rows_loaded = int(input("enter rows loaded"))
    rows_expected = int(input("enter rows expected"))

    difference = int (rows_expected - rows_loaded)
    percent = float(rows_loaded / rows_expected *100)

    print ("="  * 34)
    print ( "Dataset name - ", label)
    print ("="* 34)


    print (f"{'Rows loaded':<20} : {rows_loaded:>14.2f}")
    print (f"{'Rows expected':<20} : {rows_expected:>14.2f}")
    print (f"{'Difference':<20} : {difference:>14.2f}")
    print (f"{'Percent':<20} : {percent:>14.2f} %" )

    if percent >= 100:
        print (f"{'Status':<20} : {'OVER LIMIT':>14}")
        #because we need to record OVER LIMIT count, i need to add an action so that i get the total at the end
        over_limit_count = over_limit_count + 1

    elif percent >= 90:
        print (f"{'Status':<20} : {'WARNING':>14}")

    else:
        print (f"{'Status':<20} : {'OK':>14}")

    print("=" * 34)

#now that the first round of label has been checked, we need to create a new round, hence ask for another label 

    label = input("Enter label or 'quit' to stop")

# Need to record how many rounds were OVER LIMIT using the over_limit_count at the start

print(f"Records that came back OVER LIMIT: {over_limit_count}")

#when i input the word "quit", the loop does not stop. Cannot find mistake. 
 
# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
