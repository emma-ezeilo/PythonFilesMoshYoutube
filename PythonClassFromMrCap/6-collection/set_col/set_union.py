s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}

union_set = s1.union(s2)
print(union_set)

union_set_pipe =s1 | s2
print(union_set_pipe)

rates = {1, 2, 3}
ranks = [2, 3, 4]

ratings = rates.union(ranks)
print(ratings)


i = {'Chukwulete', 'Udoka'}
ii = {"Ezekiel"}

name = i.union(ii)
print(name)