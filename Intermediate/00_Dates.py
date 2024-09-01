### Fechas ###

from datetime import datetime, date, time, timedelta

# datetime

now = datetime.now()

def print_date(date):
  print(date.year) # año
  print(date.month) # mes
  print(date.day) # día
  print(date.hour) # hora
  print(date.minute) # minutos
  print(date.second) # segundos
  print(date.microsecond) # microsegundos
  print(date.timestamp())

print_date(now)

timestamp = now.timestamp()
print(timestamp)

print(f'Hoy: {now.year}/{now.month}/{now.day}\nHora: {now.hour}:{now.minute}:{now.second}')

year_2025 = datetime(2025, 1, 1, 3)
print_date(year_2025)

# date

today = date.fromisoformat('2019-12-04')
print(today)
today = date.fromisoformat('20191204')
print(today)
today = date.fromisoformat('2021-W01-1')
print(today)

d = date(2002, 12, 31)
print(d)
print(d.replace(day=26))
d = date(2003, 12, 29).isocalendar()
print(d)
d = date(2004, 1, 4).isocalendar()
print(d)
d = date(2002, 12, 4).isoformat()
print(d)
d = date(2002, 12, 4).ctime()
print(d)

current_date = date(2020, 6, 3) # year=2020, month=6, day=3
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date.year)
print(current_date.month)
print(current_date.day)

diff = year_2025 - now
print(diff)

diff = year_2025.date() - current_date
print(diff)

# time

current_time = time(22, 35, 55) # hour=22, minute=35, second=55

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


# timedelta

start_timedelta = timedelta(days=200, seconds=100, microseconds=100, weeks=10)
end_timedelta = timedelta(days=300, seconds=120, microseconds=190, weeks=13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
print(end_timedelta / start_timedelta)
