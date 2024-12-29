import random

def secret_share(s, p):
    # Generate a random k
    k = random.randint(1, p - 1)
    print("k:", k)
    
    # Calculate the secret shares
    s1 = (s + k) % p
    s2 = (s + 2 * k) % p
    s3 = (s + 3 * k) % p
    
    return s1, s2, s3

s = 32  
p = 131
s1, s2, s3 = secret_share(s, p)

print("Original Secret:", s)
print("p:", p)
print("s1:", s1)
print("s2:", s2)
print("s3:", s3)
