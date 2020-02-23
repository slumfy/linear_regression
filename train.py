#!/usr/bin/python
import sys
import matplotlib.pyplot as plt

def Save_tetha(Tetha0,Tetha1):
	try:
		Tfile = open("tetha.csv", 'w+')
	except:
		sys.exit("cannot open tetha.csv")
	try:
		Tfile.write(str(Tetha0) + ',' + str(Tetha1))
	except:
		sys.exit("Cannot write tetha.csv")
	Tfile.close()


def predict_price(kilom, Tetha0, Tetha1):
	return (Tetha0 + (Tetha1 * kilom))

def normeData(Klm, Price):
	Nklm = []
	Nprice = []
	Min = min(Klm)
	Max = max(Klm)
	for n in Klm:
		Nklm.append((n - Min)/(Max - Min))
	Min = min(Price)
	Max = max(Price)
	for n in Price:
		Nprice.append((n - Min)/(Max - Min))
	return (Nklm,Nprice)

def denorme(Tetha0, Tetha1,Klm, Price):
	T0 = 0.0
	T1 = 0.0
	M0 = max(Price)
	m0 = min(Price)
	M1 = max(Klm)
	m1 = min(Klm)
	T0 = (M0 -m0) * (Tetha0 - ((Tetha1 * m1) / (M1 - m1))) + m0
	T1 = Tetha1 * ((M0 - m0) / (M1 - m1))
	return(T0, T1)


try:
	File = open(sys.argv[1], "r")
except:
	sys.exit("Need a valid data.scv file")
content = File.readlines()
content.pop(0)
File.close()

Klm = []
Price = []
for i in content:
	Split = i.split(',')
	if len(Split) != 2:
		sys.exit("Bad scv format")
	Split[1] = Split[1][:-1]
	Klm.append(float(Split[0]))
	Price.append(float(Split[1]))

Nklm, Nprice = normeData(Klm,Price)
Tetha0 = 0.0
Tetha1 = 0.0
length = len(Nklm)
learnRate = 0.1
try:
	itteration = int(sys.argv[2])
except:
	sys.exit("Bad itteration number")
for n in range(itteration):
	tmpt0 = 0
	tmpt1 = 0
	for i in range(length):
		tmpt0 += (predict_price(Nklm[i], Tetha0, Tetha1) - Nprice[i])
		tmpt1 += ((predict_price(Nklm[i], Tetha0, Tetha1) - Nprice[i]) * Nklm[i])
	Tetha0 -= tmpt0 * learnRate / length 
	Tetha1 -= tmpt1 * learnRate / length

Tetha0 , Tetha1 = denorme(Tetha0, Tetha1, Klm, Price)
Save_tetha(Tetha0,Tetha1)
print "t0 = " + str(Tetha0) + " t1 = " + str(Tetha1)
Prediction = []
for x in Klm:
	Prediction.append(predict_price(x,Tetha0, Tetha1))
plt.plot(Price, Klm ,'o', Prediction, Klm)
plt.ylabel("Kilometrage")
plt.xlabel("Prix")
plt.show()
