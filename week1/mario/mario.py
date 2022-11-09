def print_slash(height):
    for i in range(height):
        for j in range(height-1-i):
            print(' ',end='')
        for j in range(i):
            print('#',end='')
        print('  ',end='')
        for j in range(i):
            print('#',end='')
        print('\n')

print('please enter height:',end='')
height = int(input())
while(height < 1 or height > 8):
    print('please enter height:',end='')
    height = int(input())

print_slash(height+1)
