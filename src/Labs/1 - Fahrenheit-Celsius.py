fahrenheit = float(input("Enter temperature in Fahrenheit:"))
celsius = ((fahrenheit - 32) * 5)/9
print ("Temperature in Celsius:", "{:.0f}".format(celsius))
if celsius >= 30:
    print ("That's Hot!")
else:
    print ("That's not hot")
