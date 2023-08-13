# Random numbers

import random
x = random.randint(10, 99) # randint function includes both numbers so in this case it will give us random 2 digit number
print(f"Random number with randint function: {x}")

y = random.random() # random function give us a random float number between 0 and 0.999999 
print(f"Random number with random function: {y}")
