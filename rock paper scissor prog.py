# Write your code here :-)
import random,sys
print('ROCK,PAPER,SCISSOR')
win=0
loss=0
tie=0
while True:
    print('%s win %s loss %s tie' %(win,loss,tie))
    while True:
        print('enter your move: (r)ock,(p)aper,(s)cissor or (q)uit')
        playermove=input()
        if playermove=='q':
            sys.exit
        if playermove=='r' or playermove=='p' or playermove=='s':
            print('type one of r,p,s or q')
            if playermove=='r':
                print('ROCK versus....')
            elif playermove=='p':
                    print('PAPER versus....')
            elif playermove=='s':
                    print('SCISSOR versus....')
        random_number=random.randint(1,3)
        if random_number==1:
            computermove='r'
            print('ROCK')
        elif random_number==2:
            computermove='p'
            print('PAPER')
        elif random_number==3:
            computermove='s'
            print('SCISSOR')
        if computermove==playermove:
            print('it is tie')
            tie=tie+1
        elif playermove=='r' and computermove=='s':
            print('you win!')
            win=win+1
        elif playermove=='p' and computermove=='r':
            print('you win!')
            win=win+1
        elif playermove=='s' and computermove=='p':
            print('you win!')
            win=win+1
        elif playermove=='r' and computermove=='p':
            print('you loss')
            loss=loss+1
        elif playermove=='p' and computermove=='s':
            print('you loss')
            loss=loss+1
        elif playermove=='s' and computermove=='r':
            print('you loss')
            loss=loss+1



