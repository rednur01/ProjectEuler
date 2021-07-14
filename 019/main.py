# Counting Sundays

# Assign indices to each day of the week
# Sunday=0, Monday=1,...Saturday=6

# Tricky part of the question: 1/1/1900 is given as monday
# but sunday counting starts from 1901

month_days_in_year: list[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_days_in_leap_year: list[int] = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year: int) -> bool:
  return (year % 4 == 0 and 
         (year % 100 != 0 or year % 400 == 0))

start_year: int = 1900
end_year: int = 2000
start_day: int = 1 #Monday

total_sundays: int = 0
day: int = start_day

for year in range(start_year, end_year+1):
  months: list[int] = month_days_in_leap_year if is_leap(year) else month_days_in_year
  for month_index, month_days in enumerate(months):
    if year != 1900 and day % 7 == 0:
      total_sundays += 1
      print(f"{month_index+1}/{year}")
    day = (day + month_days) % 7

print(total_sundays)
