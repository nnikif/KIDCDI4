import datetime

def read_datetime(date1):
    return date1.day,date1.month,date1.year

if __name__ == '__main__':
    date1=datetime.date(1990,11,25)
    print(date1)
    day1,month1,year1=read_datetime(date1)
    print(day1,month1,year1)