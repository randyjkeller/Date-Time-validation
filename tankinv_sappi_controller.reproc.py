#!/bin/python

# check for modules
import datetime
import time


def check_date():   # add both functions
    print("Enter Date (Format: YYYY/MM/DD): ")

    while True:
        try:
            date_format = '%Y/%m/%d'
            date_string = str(input())
            date_obj = datetime.datetime.strptime(date_string, date_format)
        except ValueError:
            print("Incorrect date format, should be YYYY/MM/DD:")
            continue
        else:
            break
    return date_string


def check_time():
    print("Enter time (Format: HH:MM:SS): ")

    while True:
        try:
            time_format='%H:%M:%S'
            time_string = str(input())
            time_obj=time.strptime(time_string, time_format)
        except ValueError:
            print("Incorrect time format, should be HH:MM:SS:")
            continue
        else:
            break
    return time_string


if __name__ == '__main__':
    date_string = check_date()
    time_string = check_time()

    # Calculate time
    start_time=time.mktime(time.strptime('2018/10/14 23:31:01', '%Y/%m/%d %H:%M:%S'))
    start_time2=time.mktime(time.strptime(date_string + " " + time_string, '%Y/%m/%d %H:%M:%S'))

print ("Date is " + date_string)
print ("Time is " + time_string)

# Use Original date and time as check for calculations
print ("Original time: 2018/10/14: " + str(start_time))  # correct value for org date/time 1539577861.0
print ("New time:                  " + str(start_time2))
print (" ")


