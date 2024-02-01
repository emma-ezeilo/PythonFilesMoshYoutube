from datetime import datetime

str_parse_format = datetime.strptime('5/5/2019', '%d/%m/%Y')
print(str_parse_format)

date_obj = datetime(2018, 5, 12, 2, 25, 50, 13)

formated_date = date_obj.strftime("%b %d %Y %H:%M:%S")
print(formated_date)

