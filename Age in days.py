days = int(input())
year = days//365

rem_days = days - (year*365)

months = rem_days//30

day = rem_days - (months * 30)

print("%d ano(s)" % (year))
print("%d mes(es)" % (months))
print("%d dia(s)" % (day))
