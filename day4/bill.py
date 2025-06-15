import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#option1
friends_bill = random.randint(0, 4)
print(friends[friends_bill])

#option2
fb = random.choice(friends)
print(fb)
