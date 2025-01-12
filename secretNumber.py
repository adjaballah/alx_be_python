import random;

secret_number =  random.randint(1,10)

guess = int(input("I'm thinking of a nulber between 1 and 10. Can you guess it?"))

match guess:

    case g if  guess == secret_number :
            print("Congratulation, you guessed it!")
            
    case g if guess > secret_number :
        print("Oooops, your guess is a bit high. Try again!")
    case g if guess < secret_number :
        print("Nope, your guess is a bit low . give it another shot!")   
 