A= int(input("enter number: "))
if A%3 == 0 and A%5 == 0:
    print("FIZZBUZZ")
elif A%3 == 0:
    print("FIZZ")
elif A%5 == 0:
    print("BUZZ")
else:
    print("A")