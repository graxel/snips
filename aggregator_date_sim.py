import random
import datetime
import sys

def get_group_info(week_start):
    
    group_dates = []
    
    num_groups = random.randint(1,6)
    
    one_week = datetime.timedelta(weeks=1)   
    
    for n in range(num_groups):  
        d = one_week*random.randint(0,100)/100
        group_dates.append(week_start + d) 
        
    return group_dates


def download_and_store_stories(from_date, to_date):
    
    one_week = datetime.timedelta(weeks=1)
    
    #request
    
    if random.randint(0,10) == 7:
        print("limit reached, waiting 10 sec\n") 
        error_code = 529
    else:
        error_code = 200
    	
    weekfrac = int(10 * (to_date - from_date) / one_week) 
    #print("  from_date: ", from_date)
    #print("  to_date:   ", to_date)
    #print("  weekfrac:  ", weekfrac)
    shift_int = random.randint(0, weekfrac) / 10
    
    #storage loop
    
    pub_date = from_date + (shift_int * one_week)
    
    #sql code
    
    if error_code == 200:
        earliest_stored = pub_date
    else:
        earliest_stored = to_date
    
    return error_code, earliest_stored



###############################################
###############################################

print("=============================",
      "===================\n", sep="")

one_week = datetime.timedelta(weeks=1)
one_second = datetime.timedelta(seconds=1)
now = datetime.datetime.now()
midnight = now.replace(hour=0,minute=0,second=0,microsecond=0)

this_week = midnight - datetime.timedelta(days = now.weekday())

three_back_start = (this_week + datetime.timedelta(weeks = -3)).strftime("%m/%d")
three_back_end = (this_week + datetime.timedelta(weeks = -3, days = 6)).strftime("%m/%d")

two_back_start = (this_week + datetime.timedelta(weeks = -2)).strftime("%m/%d")
two_back_end = (this_week + datetime.timedelta(weeks = -2, days = 6)).strftime("%m/%d")

one_back_start = (this_week + datetime.timedelta(weeks = -1)).strftime("%m/%d")
one_back_end = (this_week + datetime.timedelta(weeks = -1, days = 6)).strftime("%m/%d")

this_week_start = (this_week).strftime("%m/%d")
this_week_end = (this_week + datetime.timedelta(days = 6)).strftime("%m/%d")

print("3: ", three_back_start, "-", three_back_end)
print("2: ", two_back_start, "-", two_back_end)
print("1: ", one_back_start, "-", one_back_end)
print("0: ", this_week_start, "-", this_week_end)

weeks_back = int(input("\nSelect a week >> "))
week_begin = this_week - datetime.timedelta(weeks = weeks_back)
week_end = week_begin + one_week - one_second

earliest_dates = get_group_info(week_begin)

num_groups = len(earliest_dates) 

count = 0

print("\nFor week of", week_begin.strftime("%m/%d"), "-", week_end.strftime("%m/%d"), "\n")

while max(earliest_dates) > week_begin:
    	
    for group, earliest_date in enumerate(earliest_dates):
    
        if earliest_date == week_begin:
            continue
        
        error_code, earliest_date_dled = download_and_store_stories(
            week_begin, earliest_date - one_second)
        count += 1
        if error_code == 200:
            earliest_dates[group] = earliest_date_dled
        
    for group, earliest_date in enumerate(earliest_dates):
        progress = int(1000 * (week_begin + one_week - earliest_date) // one_week) / 10 
        extra_space = ""
        if progress < 100:
            extra_space = " "
        if progress < 10:
            extra_space = "  "
        print("Group ", group, "   ", earliest_date.strftime("%m/%d %H:%M:%S"),
        "   ", extra_space, progress, "%", sep="") 

    print("request count:", count, "\n") 




