from phe import paillier
import numpy as np
import pandas as pd
import pickle 


DataFrame = pd.read_csv("endpoint0.csv")
DataFrame = DataFrame[ : 100]

FiscalQuarter = list(DataFrame['Fiscal Quarter'])
Bureau = list(DataFrame ['Bureau'])
BasePay = list(DataFrame['Base Pay'])
	
publicKey, privateKey = paillier.generate_paillier_keypair()

EncryptedFiscalQuarterList = [publicKey.encrypt(x) for x in FiscalQuarter]
EncryptedBureauList = [publicKey.encrypt(x) for x in Bureau]
EncryptedBasePayList = [publicKey.encrypt(x) for x in BasePay]

with open('EncryptedData0.file', 'wb') as output:
    pickle.dump(EncryptedFiscalQuarterList, output, pickle.HIGHEST_PROTOCOL)
    pickle.dump(EncryptedBureauList, output, pickle.HIGHEST_PROTOCOL)
    pickle.dump(EncryptedBasePayList, output, pickle.HIGHEST_PROTOCOL)

# with open('EncryptedData0.file', 'rb') as input:
# EncryptedFiscalQuarterListLoad = pickle.load(input)
# EncryptedBureauListLoad = pickle.load(input)
# EncryptedBasePayListLoad = pickle.load(input)



# EncryptedNumberSum = publicKey.encrypt(0)

# for x in EncryptedBasePayList:
	# EncryptedNumberSum += x


# print(privateKey.decrypt(EncryptedNumberSum))

