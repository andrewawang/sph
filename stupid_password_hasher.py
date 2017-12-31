import bcrypt as bc
import getpass as gp
import random
import string

run = True

def main():
    while(run):
        generate()
        stop()

def stop():
    yn = input("Continue? [y/n]: ").lower()

    if (yn == 'n' or yn == 'no'):
        global run
        run = False

    elif (yn != 'y' and yn != 'yes'):
        stop()

def generate():
    password = gp.getpass("Password to be hashed: ").encode('utf8')

    seed = gp.getpass("Salt seed: ")
    random.seed(seed)

    salt = '$2b$05$' + ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k = 22))
    salt = salt.encode('utf8')


    hashed = bc.hashpw(password, salt).decode("utf-8")

    def num(s):
        try:
            s = int(s)
            if s > 32:
                return big(s)
            if s < 1:
                return small(s)
            return s
    
        except ValueError:
            s = input("Input an integer value: ")
            return num(s)
    
    def big(i):
        if (i > 32):
            i = num(input("Input an integer value less than 33: "))
        return i

    def small(i):
        if (i < 1):
            i = num(input("Input an integer value greater than 0: "))
        return i

    length = num(input("Length of hash: "))
    print("Hash: " + hashed[28 : length + 28])


main()    
