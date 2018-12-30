from datetime import datetime

a = datetime.now().strftime("%Y/%m/%d")
print(a)

if str(a) == "201/01/01":
    for i in range(0,2019):
        print("happy New year!")

