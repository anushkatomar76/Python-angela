import random
import my_module

print(my_module.my_variable)

#for random whole numbers
rand_num = random.randint(1, 10)
print(rand_num)

#for random float numbers
rand_num_0_to_1 = random.random() * 10
print(rand_num_0_to_1)

random_float = random.uniform(1, 10)
#This will generate a random floating point number between 1 and 10.

#Create a coin flip program using what you have learnt about randomisation in Python.
#It should randomly print "Heads" or "Tails" everytime it is run.

random_heads = random.randint(0, 1)
if random_heads == 0:
    print("heads")
else:
    print("tails")


