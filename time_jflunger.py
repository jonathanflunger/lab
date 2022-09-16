# %%
import time

# %%
time_now = time.time()

# %%
year_seconds = 60*60*24*365.25
month_seconds = 60*60*24*30
day_seconds = 60*60*24
hour_seconds = 60*60
min_seconds = 60

months_list = [31,28,31,30,31,30,31,31,30,31,30,31]
months_list_leap = [31,29,31,30,31,30,31,31,30,31,30,31]

# %%
year_float = time_now/year_seconds
year = int(year_float)

# %%
month_float = 1 + (year_float - year)*year_seconds/month_seconds
month = int(month_float)

# %%
day_float = 1 + (year_float - year)*year_seconds/day_seconds - sum(months_list[:int(month)-1])
day = int(day_float)


# %%
hour_float = (day_float - day)*day_seconds/hour_seconds
hour = int(hour_float)


# %%
min_float = (hour_float - hour)*hour_seconds/min_seconds
min = int(min_float)


# %%
sec_float = (min_float - min)
sec = round(sec_float, 2)*60

# %%
print('THE DATE IS ' + str(1970+year) + '-' + str(month)+ '-' + str(day)+ ' ' + str(hour)+ ':' + str(min)+ ':'+str(sec)+ ' GMT')
print('THE TIME SINCE EPOCH IS: ' +str(round(time_now,4))+ ' SECONDS')

# %%



