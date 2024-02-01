from datetime import date

my_dob = date(2000,3,19)
print(my_dob)

today_day = my_dob.today()
print(today_day)

year_res = today_day.year
print(year_res)

month_res = today_day.month
print(month_res)

day_res = today_day.day
print(day_res)