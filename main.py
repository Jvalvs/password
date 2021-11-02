import sys
import random 
import string 

def random_pass(size=16, chars=string.ascii_letters + string.punctuation + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

if __name__ == "__main__":
    args = sys.argv
    passwords = {}
    if args[1] == "new":
        passwords[args[2]] = ''
        if len(args) == 4:
           passwords[args[2]] = args[3]
        else: passwords[args[2]] = random_pass()
    
    print(passwords)     