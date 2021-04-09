from datetime import datetime

odds={1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59}
evens={2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58}

#odds=""
#print(odds)
#print(evens)

minute = datetime.today().minute
#minute2 =datetime.today().minute
print(minute)
if minute in odds:
    print("the minute is odds")
elif minute in evens:
    print("the minute is even")

#print(minute)





#print("hello world")
