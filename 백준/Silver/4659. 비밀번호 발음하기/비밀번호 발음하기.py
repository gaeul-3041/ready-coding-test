vowel = ['a', 'e', 'i', 'o', 'u']
except_double = ['ee', 'oo']

while True:
    pw = input()
    if pw == 'end':
        break
        
    chk1 = 0
    
    for p in pw:
        if p in vowel:
            chk1 += 1
            
    if chk1 == 0:
        print(f'<{pw}> is not acceptable.')
        continue
        
    flag = 1
        
    for i in range(len(pw)-2):
        chk2 = 0
        for j in range(3):
            if pw[i+j] in vowel:
                chk2 += 1
        if chk2 == 0 or chk2 == 3:
            flag = 0
            break
    
    if flag == 0:
        print(f'<{pw}> is not acceptable.')
        continue
            
    for i in range(len(pw)-1):
        piece = pw[i:i+2]
        if piece[0] == piece[1] and piece not in except_double:
            flag = 0
            break
            
    if flag == 0:
        print(f'<{pw}> is not acceptable.')
        continue
        
    print(f'<{pw}> is acceptable.')