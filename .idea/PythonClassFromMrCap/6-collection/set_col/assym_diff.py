s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

s = s1.symmetric_difference(s2)
print(s)


scores = {7, 8, 9}
ratings = {8, 9, 10}

new_set = scores.symmetric_difference(ratings)
print(new_set)

scores = {7, 8, 9}
ratings = {8, 9, 10}

new_set2 = scores ^ ratings
print(new_set2)