time = int(input())

hr = time//3600
rem_time = time - (hr*3600)
min = rem_time//60

sec = rem_time - (min*60)

print("%d:%d:%d" % (hr, min, sec))
