import re
# 这个纯属折腾人了，其实calendar可以检测是否是闰年，datetime可以识别是否是正确时间。
def leapYear(year):
    year = int(year)
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

leap_year = {'01': 31, '03': 31, '05': 31, '07': 31, '08': 31, '10': 31,
             '12': 31, '02':29, '04': 30, '06': 30, '09': 30, '11': 30}
noleap_year = leap_year.copy()
noleap_year['02'] = 28

def dateFormat(date):
    datePattern = re.compile(r"""
        ^(.*?)						# all text before the date
        ((?:0?[1-9]|[12]\d|3[01]))/ # one or two digits for the day 1-31
        ((?:0?[1-9]|1[0-2]))/       # one or two digits for the month 1-12
        ((?:19[0-9]|2[0-9][0-9])\d)      # four digits for the year 1900-2999
        (.*?)$  
        """, re.VERBOSE| re.DOTALL)

    date_temp = datePattern.search(date)

    error_message = 'Please input right date format DD/MM/YYYY,such as 3/2/2002 or 03/02/2002.'

    try:
        _, day, month, year, _ = date_temp.groups()
        if len(month) == 1:
            month = '0' + str(month)
        if len(day) == 1:
            day = '0' + str(day)

        dateformat = day + '/' + month + '/' + year

        if leapYear(year):
            if int(day) <= leap_year[month]:
                print(dateformat)
            else:
                print(error_message)
        else:
            if int(day) <= noleap_year[month]:
                print(dateformat)
            else:
                print(error_message)
    except:
        print(error_message)