import random

print("Time for toss, Enter 0 for Heads and 1 for Tails")
choice = int(input())
k = random.randint(0, 1)
if k == choice:
    print("You have won the toss")
    print("Select 0 to bat , 1 to bowl ")
    ch = int(input())
    if ch == 1:
        print("You chose to bowl")
        r = 0
    else:
        print("You chose to bat")
        r = 1
else:
    print("Computer won the toss")
    r = random.randint(0, 1)
    if r == 0:
        print("Computer chose to bat")
        ch = 1
    else:
        print("Computer chose to bowl")
        ch = 0

if ch == 1 and r == 0:
    print("Enter numbers between 1 and 6. If you both choose the same number then computer is out")
    sum = 0
    out = 0
    while out != 1:
        bowl1 = int(input())
        if bowl1 > 6 or bowl1 == 0:
            print("Enter valid choice")
            continue
        r1 = random.randint(1,6)
        print("User chose ", bowl1)
        print("Computer chose ", r1)
        if r1 != bowl1:
            sum = sum + r1
            print("Computer score is ", sum)
        else:
            print("Computer is out")
            print("Final computer score is ", sum)
            out = 1

    print("Enter numbers between 1 and 6. If you both choose the same number then user is out")
    sum1 = 0
    out1 = 0
    while out1 != 1:
        bat1 = int(input())
        if bat1 > 6 or bat1 == 0:
            print("Enter valid choice")
            continue
        r1 = random.randint(1,6)
        print("User chose ", bat1)
        print("Computer chose ", r1)
        if r1 != bat1:
            sum1 = sum1 + bat1
            print("User score is ", sum1)
            if sum1 > sum:
                break
        else:
            print("User is out")
            print("Final user score is ", sum1)
            out1 = 1
    if sum1 > sum:
        print("User win")
    elif sum > sum1:
        print("Computer wins")
    else:
        print("Match draw")

elif ch == 0 and r == 1:
    print("Enter numbers between 1 and 6 .If you both choose the same number then user is out")
    sum = 0
    out = 0
    while out != 1:
        bat1 = int(input())
        r1 = random.randint(1,6)
        print("User chose ", bat1)
        print("Computer chose ", r1)
        if r1 != bat1:
            sum = sum + bat1
            print("User score is ", sum)
        else:
            print("User is out")
            print("Final user score is ", sum)
            out = 1

    print("Enter numbers between 1 and 6. If you both choose the same number then computer is out")
    sum1 = 0
    out1 = 0
    while out1 != 1:
        bat1 = int(input())
        r1 = random.randint(1,6)
        print("User chose ", bat1)
        print("Computer chose ", r1)
        if r1 != bat1:
            sum1 = sum1 + r1
            print("Computer score is ", sum1)
            if sum1 > sum:
                break
        else:
            print("Computer is out")
            print("Final computer score is ", sum1)
            out1 = 1
    if sum1 < sum:
        print("User win")
    elif sum < sum1:
        print("Computer wins")
    else:
        print("Match draw")
