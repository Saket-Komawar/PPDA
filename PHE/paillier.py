from phe import paillier

publicKey, privateKey = paillier.generate_paillier_keypair()

numberList = [1, 2, 3, 4, 5]

encryptedNumberList = [publicKey.encrypt(x) for x in numberList]

encryptedNumberSum = publicKey.encrypt(0)

for x in encryptedNumberList:
	encryptedNumberSum += x


print(privateKey.decrypt(encryptedNumberSum))