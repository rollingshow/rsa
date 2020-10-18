
import math
import random
import base64
def generatenumbers(start):
    count = start
    
    while True:
        isprime = True
        
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                break
   
        if isprime:
            return (count)
        count += 1

def getpqe():
    random.seed(a=None, version=3)
    p=generatenumbers(random.randint(2,17))
    q=generatenumbers(p+1)
    array = [3,5,17,257,65537]
    e = 0
    for arr in array:
        if(arr<p*q):
            e=arr
    return(p,q,e)


def rsa_encrypt(message, public_key):
    e = public_key[0]
    n = public_key[1]
    en_m = []
    for i in message:
        i = ord(i)
        encoded = (i ** e ) % n
        en_m.append(encoded)
    return en_m 

def rsa_decrypt(message, private_key):
    d = private_key[0]
    n = private_key[1]
    de_m = []
    for i in message:
        i = int(i)
        decoded = (i ** d ) % n
        decoded = chr(decoded)
        de_m.append(decoded)
    return de_m 


def encrypt_base64(message):
    enc = []
    for i in message:
        b64 = b6.b64encode(bytes(str(i), 'ascii'))
        enc.append(b64)
    return enc

def decrypt_base64(message):
    enc = []
    for i in message:
        b64 = b6.b64decode(i)
        enc.append(b64)
    return enc

def concat(message):
    done = ""
    for i in message:
        i = str(i)
        done += i
    return done


if __name__== "__main__":
    get=getpqe()
    print(get)
    n=get[0]*get[1]
    funcel=(get[0]-1)*(get[1]-1)
    d = 0
    while ((d * get[2]) % (funcel)) != 1:
        d +=1       
    print("d =", d) 
    public_key = (get[2], n)
    private_key = (d, n)
    print(get[0], get[1])
    print("public key = ", public_key)
    print("private key = ", private_key)
    message = input("Enter message:")
    result=rsa_encrypt(message, public_key)
    print(result)
    print(rsa_decrypt(result, private_key))
   
    


        
