#!/usr/bin/python
import sys
import matplotlib.pyplot as plt

def predict_price(kilom, Tetha0, Tetha1):
	return (Tetha0 + (Tetha1 * kilom))

def mean(list):
	sum = 0
	l = len(list)
	for x in range(l):
		sum += list[x]
	return(sum / l)

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
print Nklm
print Nprice
Tetha0 = 0.0
Tetha1 = 0.0
length = len(Nklm)
learnRate = 0.1
itteration = int(sys.argv[2])
for n in range(itteration):
	tmpt0 = 0
	tmpt1 = 0
	for i in range(length):
		tmpt0 += (predict_price(Nklm[i], Tetha0, Tetha1) - Nprice[i])
		tmpt1 += ((predict_price(Nklm[i], Tetha0, Tetha1) - Nprice[i]) * Nklm[i])
	Tetha0 -= tmpt0 * learnRate / length 
	Tetha1 -= tmpt1 * learnRate / length
print "oldt0 " + str(Tetha0)
print "oldt1 " + str(Tetha1)

Tetha0 , Tetha1 = denorme(Tetha0, Tetha1, Klm, Price)
print "t0 " + str(Tetha0)
print "t1 " + str(Tetha1)


Prediction = []
for x in Klm:
	Prediction.append(predict_price(x,Tetha0, Tetha1))
print Klm
print Prediction
plt.plot(Price, Klm ,'o', Prediction, Klm)
plt.ylabel("Kilometrage")
plt.xlabel("Prix")
plt.show()
