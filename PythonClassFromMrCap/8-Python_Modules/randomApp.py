import random

rnd = random.random()
print(rnd)

leader = random.choice(['Kola', 'John', 'Paul', 'Peter', 'Dorcas'])
print(leader)

rnd2 = random.random() * 1000
roun_val = round(rnd2)
print(roun_val)

res_rand = random.randint(1,10)
print(res_rand)

fn = random.randint(1,10)
sn = random.randint(1,10)
res = fn + sn
print(res)

rand_range = random.randrange(20, 500, 5)
print(rand_range)