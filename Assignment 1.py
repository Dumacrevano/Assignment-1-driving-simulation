velocity = 0
time_on_road = int(input("Time:\n"))
acceleration = int(input("Acceleration:\n"))
Dist = int(input("Distance:\n"))
Speed_lim = 60
v = velocity + acceleration * time_on_road   # speed at the end of journey formula
s = velocity*time_on_road + (acceleration / 2 * time_on_road ** 2)  # reached distance formula
x = 0
print("one * represent 10M:")
while x < time_on_road:
    x = x + 1
    s = velocity + (acceleration / 2 * x ** 2)
    y = int(s / 10) * "*"
    print("duration" + str(x) + "=" + y)
if v >= 60:
    print("speed limit exceeded,(the speed is " + str(v) + "M/S)")
else:
    print("speed under the limit"+"(,the speed is " + str(v) + "M/S)")
if s >= Dist:
    print("you have reached your destination"+" (destination reached"+ str(s)+"M)")
else:
    print("you dont reach your destination"+" (destination reached"+ str(s) +"M)")
