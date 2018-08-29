def encrypt(s):
     s1="&".join(s)
     s2=''
     for i in range(len(s1)):
          s2+=chr(ord(s1[i])+5)
     return s2

def Decrypt(s):
     s1=''
     for i in s:
          s1+=chr(ord(i)-5)
     s1=s1[::2]
     return ''.join(s1)

print("BEFORE Encryption")

print()

print("Triple DES. Triple DES was designed to replace the original Data Encryption Standard (DES) algorithm, which hackers eventually learned to defeat with relative ease. ...")

print()

print("AFTER ENCRYPTION")

print()

print(encrypt("Triple DES. Triple DES was designed to replace the original Data Encryption Standard (DES) algorithm, which hackers eventually learned to defeat with relative ease. ..."))

print()

print("After DECRYPTION")

print()

print(Decrypt(encrypt("Triple DES. Triple DES was designed to replace the original Data Encryption Standard (DES) algorithm, which hackers eventually learned to defeat with relative ease. ...")))

