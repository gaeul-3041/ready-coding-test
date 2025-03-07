n, game = input().split()
people = set()

for i in range(int(n)):
    people.add(input())
    
m = len(people)
if game == 'Y':
    print(m)
elif game == 'F':
    print(m // 2)
elif game == 'O':
    print(m // 3)