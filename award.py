Swim = int(input("Total swim duration in minutes is: "))
Cyc = int(input("Total cycling duration in minutes is: "))
Run = int(input("Total running duration in minutes is: "))

Total_duration = sum([Swim, Cyc, Run])
print ("Your total duration for the Triathlon is: " + str(Total_duration))

if Total_duration <= 100:
    print ("Congratulations!!! You are awarded the Provincial colours.")
elif Total_duration >= 101 and Total_duration <=105:
    print ("Congratulations!!! You are awarded the Provincial half colours.")
elif Total_duration >= 106 and Total_duration <=110:
    print ("Congratulations!!! You are awarded the Provincial scroll.")
else:
    print ("Welldone! No Award. Try again next time")