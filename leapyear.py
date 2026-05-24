# LEAP YEAR CODE
# when earth rotates the sun in 365.25 days 
# according to calender they consider as 0.25*4 == 1 day, this one day added to february in leap year
# according to calender rule every 00 year can't have the leap year because earth takes the less time 
# so they added one leap year for every 400 years

year=int(input("enter the year: "))
if (year%400==0) or (year%4==0 and year%100!=0):
    print("This is leap year")
else:
    print("This is not leap year")