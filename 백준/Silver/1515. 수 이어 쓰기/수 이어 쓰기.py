def increase():
    num = 0
    i = 0
    
    while True:
        num += 1
        for s in str(num):
            if number[i] == s:
                i += 1
                if i == len(number):
                    return num


number = input()
print(increase())