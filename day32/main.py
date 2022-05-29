import datetime as dt

now_year = dt.datetime.now().year
now_month = dt.datetime.now().month
now_day = dt.datetime.now().day
now_week = dt.datetime.now().weekday() + 1
print(f"今天是: {now_year} 年 {now_month} 月 {now_day} 日 星期 {now_week}")
