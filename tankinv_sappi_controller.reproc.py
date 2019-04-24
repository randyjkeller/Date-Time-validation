#!/bin/python
import datetime
import time

def gather_info():
    #validate User Input Function
    date_string=input("Enter Date (Format: YYYY/MM/DD) ")
    date_format='%Y/%m/%d'
    time_string=input("Enter Time (Format: HH:MM:SS) ")
    time_format='%H:%M:%S'

    # Validate Date
    try:
        date_obj=datetime.datetime.strptime(date_string, date_format)
    except ValueError:
        print("Incorrect date format, should be YYYY/MM/DD")
        gather_info()
    # Validate Time
    try:
        time_obj=datetime.datetime.strptime(time_string, time_format)
    except ValueError:
        print("Incorrect time format, should be HH:MM:SS")
        gather_info()

    return(date_string,time_string)

while True:
    date_string,time_string = gather_info()
    start_time=time.mktime(time.strptime('2018/10/14 23:31:01', '%Y/%m/%d %H:%M:%S'))
    start_time2=time.mktime(time.strptime(date_string + " " +  time_string, '%Y/%m/%d %H:%M:%S'))
    # Use Original date and time as check for calculations
    print ("Original time: 2018/10/14: " + str(start_time)) # correct value for org date/time 1539577861.0
    print ("New time:                  " + str(start_time2))
    print (" ")