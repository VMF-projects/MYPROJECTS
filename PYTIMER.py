import time
while True:
    try:
        time_nub=int(input("How much time: "))
        break
    except:
        print("Not valid")
while time_nub!=0:
    for qds453 in range(time_nub):
        time_nub-=1
        print(f"Seconds left: {time_nub}")
        time.sleep(1)
print("Time out")