import time
timestamp=(time.strftime('%H:%M:%S'))
print(timestamp)

# This variable holds the int value of hour
timestamp1=int(time.strftime('%H'))

# if the value of hour is less than 12 then it will greet good morning
if(timestamp1<12):
    print("Good Morning Sir")

# if the value of hour is between 12 and 16 then it will greet good afternoon
elif(12<timestamp1<16): 
    print("Good Afternoon Sir")
else:
    print("Good Evening Sir")
exit()