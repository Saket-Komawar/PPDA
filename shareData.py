from phe import paillier 
import codecs
import csv
import pickle 

reader = csv.reader(codecs.open('Age.csv', 'rU', 'utf-16'))

sum = 0

# enter col on which avg = find
col = 'Age'
colNum = 1

#find average 
for index, row in enumerate(reader):
	if index != 0:
		sum = sum + int(row[colNum])
	else :
	    for index1, num in enumerate(row):
    	    # get col number by reading first row
	        if col in num: 
	            colNum = index1
	            print (colNum)
	            break
	    print (row)
avg = sum/index
print ("average is ", avg)


#GenerationOfKey
public_key, private_key = paillier.generate_paillier_keypair()
secret_number_list = [avg]

#encryption
encrypted_number_list = [public_key.encrypt(x) for x in secret_number_list]
print ("\nencrypted: ", encrypted_number_list)

with open('encrypted_data.file', 'wb') as output:
    pickle.dump(encrypted_number_list, output, pickle.HIGHEST_PROTOCOL)

with open('encrypted_data.file', 'rb') as input:
    company1 = pickle.load(input)
    print(company1) 

#decryption
orgList = [private_key.decrypt(x) for x in encrypted_number_list]
print ("Decrypted: ", orgList)

#Operations on encrypted Data
encrypted_number_list.append(1)
a, b = encrypted_number_list
a_plus_5= a+5

print ("\navg + 5 in encrypted :", a_plus_5)
d = private_key.decrypt(a_plus_5)

print ("Decrypted", d)


