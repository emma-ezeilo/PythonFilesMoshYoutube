def multi():
    nums = range(1,25)
    for num in nums:
        if num == 8:
            break
        res = f'10 times {num} is {10*num}'
        print(res)
        

multi()  