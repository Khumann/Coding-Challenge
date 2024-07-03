def prime(num):
        '''
        check for prime number
        '''
        # checking even and 1
        if num == 1 or (num % 2 == 0 and num != 2):
            return False
        # checking odd for prime
        i = 3
        while i < num:
            if num % i == 0:
                return False
            i += 2
        return True



def get_factor(num):
    '''
    make a list of prime numbers
    '''
    factors = []
    i = 2
    while i < num:
        if num % i == 0:
            factors.append(i)
        i += 1
    return factors


def check_prime(num):
    if prime(num):
        print("prime")
    else:
        print("Number is composite and its factors are:", get_factor(num))


def gen_prime(low, high):
    print("Function To be implemented")
    pass


if "__main__" == __name__:
    while True:
        print("Enter your Choice: ")
        print(" For Prime: 1")
        print(" For Generate in range: 2")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            number = int(input("Enter number to check: "))
            check_prime(number)
        elif choice == 2:
            lower = int(input("Enter lower bound: "))
            upper = int(input("Enter upper bound: "))
            gen_prime(lower, upper)
        else:
            print("invalid input")
            
        
        choice = input("Do you want to exit (Y/N): ")
        if choice == "Y" or choice == "y":
            break
        elif choice == "N" or choice == "n":
            continue
        else:
            print("invalid input")






