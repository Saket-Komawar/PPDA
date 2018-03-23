from phe import paillier
import numpy as np
import pandas as pd
import pickle 
import time
from PIL import Image


publicKey, privateKey = paillier.generate_paillier_keypair()

fileR = open("numberOfrows-time-encryptions.csv", "w+")


n = 1000
while(n <= 10000):
	start = time.clock()
	print(n)
	DataFrame = pd.read_csv("endpoint0.csv")
	DataFrame = DataFrame[ : n]


	FiscalQuarterList = list(DataFrame['Fiscal Quarter'])
	BureauList = list(DataFrame ['Bureau'])
	BasePayList = list(DataFrame['Base Pay'])

	print(1)
	EncryptedBasePayList = [publicKey.encrypt(x) for x in BasePayList]
	print(2)
	file = 'EncryptedData0.file ' + str(n)

	with open(file, 'wb') as output:
		pickle.dump(BasePayList, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(publicKey, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(privateKey, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(FiscalQuarterList, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(BureauList, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(EncryptedBasePayList, output, pickle.HIGHEST_PROTOCOL)

	print(3)	
	end = time.clock()
	elapsed = end - start
	print(elapsed)
	fileR.write(str(n) + "," + str(elapsed) + "\n")
	n += 1000


