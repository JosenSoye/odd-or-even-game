import random
def toss(x, y, d, a):
    if d!='odd' and d!='even':
        print('invalid value')
        d=input('odd or even')
        toss(x,y,d,a)
    if (x + y) % 2 == 0:
        if d.lower() == 'even':
            print(a, 'won the toss')
            print('Choose to bat')
        else:
            print('com won the toss')
            print('Choose to bowl')
    else:
        if d.lower() == 'odd':
            print(a, 'won the toss')
            print('Choose to bat')
        else:
            print('com won the toss')
            print('Choose to bowl')

def pbat(a, s=0):
    while True:
        b = int(input('Enter the batting value (1-6): '))
        if b > 6 or b < 1:
            print('Invalid score. Enter a number between 1 and 6.')
            continue
        c = random.randint(1, 6)
        print(a, 'puts', b)
        print('com puts', c)
        if b == c:
            print('Out!')
            print('Total score:', s)
            break
        else:
            s += b
            print('The score is', s)
    return s

def cbat(f, a, s=0):
    while True:
        c = int(input('Enter the bowling value (1-6): '))
        if c > 6 or c < 1:
            print('Invalid score. Enter a number between 1 and 6.')
            continue
        b = random.randint(1, 6)
        print('com puts', b)
        print(a, 'puts', c)
        if b == c:
            print('Out!')
            print('Total score:', s)
            break
        else:
            s += b
            print('The score is', s)
            if s > f:
                print('com wins')
                break
    return s

# Main Game
a = input('Enter player name: ')
d = input('Odd or even: ').strip().lower()
b = int(input('Enter a number between 1 and 6: '))
c = random.randint(1, 6)
print('Player put', b)
print('com put', c)
toss(b, c, d, a)


print(a, 'bats first')
f = pbat(a)
print('\nNow com bats')
g = cbat(f, a)

if f > g:
    print(a, 'won the game')
elif f == g:
    print('The game is tied')
else:
    print('com wins the game')
