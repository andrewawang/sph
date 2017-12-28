import bcrypt as bc
import getpass as gp

password = gp.getpass("Password to be hashed: ").encode('utf8')
hashed = bc.hashpw(password, bc.gensalt()).decode("utf-8")

def num(s):
    try:
        s = int(s)
        if s > 53:
            return big(s)
        if s < 1:
            return small(s)
        return s
    
    except ValueError:
        s = input("Input an integer value: ")
        return num(s)
    
def big(i):
    while (i > 53):
        i = num(input("Input an integer value less than 54: "))
    return i

def small(i):
    while (i < 1):
        i = num(input("Input an integer value greater than 0: "))
    return i

length = num(input("Length of hash: "))
print("Hash: " + hashed[7:length + 7])

