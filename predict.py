#!/usr/bin/python
import sys

def predict_price(kilom, Tetha0, Tetha1):
	return (Tetha0 + (Tetha1 * kilom))
try:
	Tfile = open("tetha.csv", 'r+')
except:
	sys.exit("cannot open tetha.csv")
content = Tfile.readlines()
if len(content) != 1:
	sys.exit("Bad tetha.csv format")
Split = content[0].split(',')
Split[1] = Split[1][:-1]
T0 = float(Split[0])
T1 = float(Split[1])
try:
	value = float(sys.argv[1])
except:
	sys.exit("Not a valid Price")
prediction = predict_price(value,T0,T1)
if prediction > 0:
	print("The price of your car will by around: " + str(prediction))
else:
	print("Your car have no value")
