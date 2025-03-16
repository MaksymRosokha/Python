windPower = float(input("Enter the wind power: "))

if windPower < 1:
    print("Cisza")
elif windPower >= 1 and windPower <= 3:
    print("Zefir")
elif windPower >= 4 and windPower <= 27:
    print("Bryza")
elif windPower >= 28 and windPower <= 47:
    print("Wichura")
elif windPower >= 48 and windPower <= 63:
    print("Sztorm")
else:
    print("Huragan")