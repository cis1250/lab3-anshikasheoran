# "while" keeps asking the user to put a valid positive integer to meet the specific program conditions
while True:
  user_input = input("Enter the number of terms: ")
  
  if user_input.isint(): # check if the input is only integers
    n = int(user_input): 
    if n > 0: # make sure the integer is positive
      a, b = 0,1 #initialize the first two numbers of the Fibonacci sequence, 
      
      for _ in range(n): # print the fibonacci sequence using a for loop
        print(a, end=" ")
        a, b = b, a + b # the Fibonacci rule, updating numbers: next a becomes current b, next b becomes sum of previous a+b
      
      print()
      break # exit the loop
  else: 
    print("Enter a positive integer") # user entered zero or a negative integer
else: 
  print("Enter a positive integer") # user entered an invalid character
  
