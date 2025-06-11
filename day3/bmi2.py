weight = 65
height = 5.7
bmi = weight / (height ** 2)
print(bmi)
# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("overweight")



