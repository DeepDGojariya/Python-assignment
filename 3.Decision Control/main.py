#Problem 1
def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str


print(new_string("Empty"))


#Problem 2
number = int(input("Enter a number = "))
def evenOdd(number):
    if(number%2==0):
        print("Even number entered")
    else:
        print("Odd number entered")
    return

evenOdd(number)

#Problem 3
vowels = ['a','A','e','E','i','I','o','O','u','U']
def vowelCheck(character):
    if character in vowels:
        print("Vowel entered")
    else:
        print("Entered character is not a vowel.")
    return

vowelCheck(input("Enter a character: ")[0])