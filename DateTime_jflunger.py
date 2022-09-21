import time
 
SECONDS_DAY = 24*60*60
SECONDS_HOUR = 60*60
SECONDS_MIN = 60
SECONDS_YEAR = 365*24*60*60
SECONDS_CYCLE = SECONDS_YEAR*4 + SECONDS_DAY
months_days = [31,28,31,30,31,30,31,31,30,31,30,31]
months_days_leap = [31,29,31,30,31,30,31,31,30,31,30,31]

time_since_epoch = time.time() #if other timestamp is used, change here

#1st part of problem: get the time

def get_time(timestamp):
    hour = int((timestamp%SECONDS_DAY)/SECONDS_HOUR)
    min = int((timestamp%SECONDS_HOUR)/SECONDS_MIN)
    sec = int(round(timestamp%SECONDS_MIN))
    return str(hour).zfill(2)+':'+str(min).zfill(2)+':'+str(sec).zfill(2)


#2nd part of the problem: get the date
#work with 4-year cycles, where the last year is a leap year

def get_month(months_days_list, divmod_year, add_years):
    for i in range(12):
        if divmod_year[1]/SECONDS_DAY - add_years*365 - sum(months_days_list[:i]) < months_days_list[i]:
            month = i + 1
            break
    return month


def get_day(month, months_days_list, divmod_year, add_years):
    day = int(divmod_year[1]/SECONDS_DAY - add_years*365 - sum(months_days_list[:month-1]) + 1)
    return day                                                   # +1 because there is no day 0


def get_date(timestamp):

    cycles_divmod = divmod(timestamp+SECONDS_YEAR, SECONDS_CYCLE)
    cycles = cycles_divmod[0]

    if cycles_divmod[1]/SECONDS_YEAR < 3:
        extra_years = cycles_divmod[1]//SECONDS_YEAR
        month = get_month(months_days, cycles_divmod, extra_years)
        day = get_day(month, months_days, cycles_divmod, extra_years)

    else:
        extra_years = 3 #last year must be a leap year if there are more than 3 extra years
        month = get_month(months_days_leap, cycles_divmod, extra_years)
        day = get_day(month, months_days_leap, cycles_divmod, extra_years)
        
    year = int(cycles*4 + extra_years) + 1969
    return str(year)+'-'+str(month).zfill(2)+'-'+str(day).zfill(2)


def main(timestamp):
    return 'THE DATE IS: ' + get_date(timestamp) + ' ' + get_time(timestamp) + ' GMT\n\
THE TIME SINCE EPOCH IS: ' + str(round(timestamp,3)) + ' SECONDS' 


if __name__ == '__main__':
    print(main(timestamp = time_since_epoch))
