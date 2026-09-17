"""
Problem 1: Use the datetime module to calculate the number of days between two dates: June 25, 2021, and August 10, 2021.

Problem 2: Format the date August 10, 2021, in the following formats:
- Aug 10, 2021
- 10 - Aug - 2021
- 10 / Aug / 2021
- 10 / August / 2021
- Tue, 10 August 2021
"""

#                         Solution


######################### Ass_1 ##############################

import datetime

intial_date = datetime.date(2021,6,25)
final_date = datetime.date(2021,8,10)

print(f"Days From {intial_date} To {final_date} Is => {(final_date-intial_date).days}")

print("-"*50)
######################### Ass_2 ##############################


print(final_date)
print(final_date.strftime("%b %d, %Y"))
print(final_date.strftime("%d - %b - %Y"))
print(final_date.strftime("%d / %b / %Y"))
print(final_date.strftime("%d / %B / %Y"))
print(final_date.strftime("%a,%d %B %Y"))

