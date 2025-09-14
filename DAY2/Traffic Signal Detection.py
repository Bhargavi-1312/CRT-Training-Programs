#2.TRAFFIC SIGNAL DECISION
light=input("Enter the traffic light color(red, yellow, green):").strip().lower()
if light=="red":
    print("stop immediately")
elif light=="yellow":
    print("get ready to move")
elif light=="green":
    print("you can go")
else:
    print("invalid") 