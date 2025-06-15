student_scores = [180, 124, 165, 173, 189, 199, 169, 146]
total_score = sum(student_scores)
# print(total_score)

# sum = 0
#by for loops adding all the numbers
# for score in student_scores:
#     sum += score
# print(sum)
#

#find the highest number
max_score = 0

for score in student_scores:
    if max_score < score:
        max_score = score

print(max_score)

