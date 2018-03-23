import time
from phe import paillier
import numpy as np
import pandas as pd
import pickle 

fileR = open("numberOfrows-time-noise.csv", "w+")

n = 1000
while(n <= 10000):
	start = time.clock()
	print(n)
	file = 'EncryptedData0.file ' + str(n)


	with open(file, 'rb') as input:
		BasePayList = pickle.load(input)
		publicKey = pickle.load(input)
		privateKey = pickle.load(input)
		FiscalQuarterListLoad = pickle.load(input)
		BureauListLoad = pickle.load(input)
		EncryptedBasePayListLoad = pickle.load(input)

	maxB = max(BasePayList)	
	print(maxB)

	loc, scale = 0.0, (maxB / 1.5) 
	noiseList = np.random.laplace(loc, scale, len(EncryptedBasePayListLoad))
	EncryptedNoiseList = [publicKey.encrypt(x) for x in noiseList]


	EncryptedPerturbedBasePayList = []


	for i, j in zip(EncryptedBasePayListLoad, EncryptedNoiseList):
		EncryptedPerturbedBasePayList.append(i + j)

	with open(file + ".per", 'wb') as output:
		pickle.dump(publicKey, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(privateKey, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(EncryptedPerturbedBasePayList, output, pickle.HIGHEST_PROTOCOL)	

	end = time.clock()
	elapsed = end - start	
	print(elapsed)
	fileR.write(str(n) + "," + str(elapsed) + "\n")
	

	n += 1000	
	
