# Fizz Buzz Solution

def fizzbuzz(number):
    """
    fizzbuzz checks if the given number is divisible by 3, 5
    or both and returns fizz, buzz or fizzbuzz respectively.
    Otherwise, it will return the same number.
    
    Params:
    ------
        number (int): user provided number, assumed to be valid
        
    returns:
        str : Fizz if divisible by 3
        str : Buzz if divisible by 5
        str : FizzBuzz if divisible by 3 and 5
        number (int): Same same parameter provided number
    """
    
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
        
    else:
        return number
        
    
def main():
    """
    main game function. Prompts the user for a number and 
    validates user input is valid as an integer.
    
    
    Params:
    ------
        None
        
    Returns:
    -------
        None
    """
    
    user_number = input("Enter a number: ")
    
    if user_number.isdigit():
        result = fizzbuzz( int(user_number) )
        print(result)
        
    else:
        print("invalid input, quitting...")
        return 
    
    
    
if __name__ == "__main__":
    main()