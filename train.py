#!/usr/bin/python
import sys
import matplotlib.pyplot as plt

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
	Klm.append(int(Split[0]))
	Price.append(int(Split[1]))

Tetha0 = 0
Tetha1 = 0

plt.plot(Price ,Klm , 'o')
plt.ylabel("Kilometrage")
plt.xlabel("Prix")
plt.show()
