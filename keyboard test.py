import keyboard
import time
import os



start = time.time()
while True:
    end = time.time()
    os.system('cls')
    if int(end-start) <= 10:
        print(20-int(end-start))
    else:
        print("0"+str(20-int(end-start)))
    if keyboard.is_pressed("a"):
        result = "p1 wins"
        break
    if keyboard.is_pressed("l"):
        result = "p2 wins"
        break
    if end - start > 20.0:
        result = "timed out"
        break
print(result)


