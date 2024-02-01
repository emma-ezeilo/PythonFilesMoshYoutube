shoe_size =[23.7,34.6,29.4,33.6,32.99]
max_size = [big_size for big_size in shoe_size]
print(max(max_size))

nums = [2,3,4,5,6,7]
num_res = [num ** 2 for num in nums]
print(num_res)

emp = [
    ['John', 23000.89],
    ['Peter', 33000.89],
    ['Paul', 55000.89],
    ['James', 13000.89],
    ['Ruth', 23000.89]
]

high_sal =[emp for emp in emp if emp[1] > 40000]
print(high_sal)