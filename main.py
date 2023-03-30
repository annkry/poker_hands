'''During each iteration, 5 cards of the Player1 and 5 cards of the Player2 will be choosen randomly, and then the strength of the players' card combinations will be 
checked using the functions system1 and system2, which check the color and value repetitions of the cards. The strengths of the combinations are as follows:

Five of a kind  - 1
Four of a kind  - 2
Full house      - 3
Flush           - 4
Straight        - 5
Three of a kind - 6
Two pair        - 7
One pair        - 8
In the remaining combinations, Player2 wins or, if the strengths of the combinations are equal.'''

import random


F = ['A', 'K', 'Q', 'J'] # A - ace, K - king, Q - queen, J - jack - possibilities of Player2's cards
B = [2, 3, 4, 5, 6, 7, 8, 9, 10]  # possibilities of Player1's cards
losF = []
losB = []
kolF = []
kolB = []


def system2(F, c):
    if F.count(F[0]) == 4 or F.count(F[1]) == 4:
        return 2
    elif (F.count(F[0]) == 3 and (F.count(F[1]) == 2 or F.count(F[2]) == 2 or F.count(F[3]) == 2)) or (F.count(F[0]) == 2 and (F.count(F[1]) == 3 or F.count(F[2]) == 3 or F.count(F[3]) == 3)):
        return 3
    elif F.count(F[0]) == 3 or F.count(F[1]) == 3 or F.count(F[2]) == 3:
        return 6
    elif (F.count(F[0]) == 1 and (F.count(F[1]) == 2 and F.count(F[2]) == 2 and F.count(F[3]) == 2)) or (F.count(F[0]) == 2 and (F.count(F[1]) == 1 and F.count(F[2]) == 2 and F.count(F[3]) == 2)) or (F.count(F[0]) == 2 and F.count(F[1]) == 2 and F.count(F[2]) == 1 and F.count(F[3]) == 2) or (F.count(F[0]) == 2 and F.count(F[1]) == 2 and F.count(F[2]) == 2 and F.count(F[3]) == 2):
        return 7
    elif F.count(F[0]) == 2 or F.count(F[1]) == 2 or F.count(F[2]) == 2 or F.count(F[3]) == 2 or F.count(F[4]) == 2:
        return 8
    return 9


def system1(B, c):
    copyB = B.copy()
    copyB.sort()
    if c.count(c[0]) == 5 and copyB[1] == copyB[0]+1 and copyB[2] == copyB[1]+1 and copyB[3] == copyB[2]+1 and copyB[4] == copyB[3]+1:
        return 1
    elif B.count(B[0]) == 4 or B.count(B[1]) == 4:
        return 2
    elif (B.count(B[0]) == 3 and (B.count(B[1]) == 2 or B.count(B[2]) == 2 or B.count(B[3]) == 2)) or (B.count(B[0]) == 2 and (B.count(B[1]) == 3 or B.count(B[2]) == 3 or B.count(B[3]) == 3)):
        return 3
    elif c.count(c[0]) == 5 and (copyB[1] != copyB[0]+1 and copyB[2] != copyB[1]+1 and copyB[3] != copyB[2]+1 and copyB[4] != copyB[3]+1):
        return 4
    elif copyB[1] == copyB[0]+1 and copyB[2] == copyB[1]+1 and copyB[3] == copyB[2]+1 and copyB[4] == copyB[3]+1 and (c.count(c[0]) != 5):
        return 5
    elif B.count(B[0]) == 3 or B.count(B[1]) == 3 or B.count(B[2]) == 3:
        return 6
    elif (B.count(B[0]) == 1 and (B.count(B[1]) == 2 and B.count(B[2]) == 2 and B.count(B[3]) == 2)) or (B.count(B[0]) == 2 and (B.count(B[1]) == 1 and B.count(B[2]) == 2 and B.count(B[3]) == 2)) or (B.count(B[0]) == 2 and B.count(B[1]) == 2 and B.count(B[2]) == 1 and B.count(B[3]) == 2) or (B.count(B[0]) == 2 and B.count(B[1]) == 2 and B.count(B[2]) == 2 and B.count(B[3]) == 2):
        return 7
    elif B.count(B[0]) == 2 or B.count(B[1]) == 2 or B.count(B[2]) == 2 or B.count(B[3]) == 2 or B.count(B[4]) == 2:
        return 8
    return 10


count_1 = 0
count_2 = 0
for i in range(0, 100000):
    losB.clear()
    kolF.clear()
    kolB.clear()
    losF.clear()
    for j in range(0, 5):
        losF.append(random.choice(F))
        kolF.append(random.randint(1, 4))
    for j in range(0, 5):
        losB.append(random.choice(B))
        kolB.append(random.randint(1, 4))
    a = system1(losB, kolB)
    b = system2(losF, kolF)
    if a >= b:
        count_2 += 1
    else:
        count_1 += 1
print(count_1/100000)
