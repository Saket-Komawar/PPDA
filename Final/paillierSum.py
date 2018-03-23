import time
from phe import paillier
import numpy as np
import pandas as pd
import pickle 

fileR = open("numberOfrows-time-sum.csv", "w+")


n = 1000
while(n <= 10000):
	start = time.clock()

	print(n)
	file = 'EncryptedData0.file ' + str(n) + ".per"

	with open(file, 'rb') as input:
		publicKey = pickle.load(input)
		privateKey = pickle.load(input)
		EncryptedPerturbedBasePayList = pickle.load(input)

	EncryptedNumberSum = publicKey.encrypt(0)

	for x in EncryptedPerturbedBasePayList:
		EncryptedNumberSum += x


	end = time.clock()
	elapsed = end - start	
	print(elapsed)
	fileR.write(str(n) + "," + str(elapsed) + "," + str(privateKey.decrypt(EncryptedNumberSum)) + "\n")
	
	n += 1000