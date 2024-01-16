
'''

def main():
    print("Hello world!")
if __name__ == '__main__':
    main()

''

# Find the all factors of x using a loop and the operator %
# % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
x = 52633
for i in range(1,x+1):
    if(x%i==0):print(str(i) + " ", end="")
# Write a function that prints all factors of the given parameter x

print("new code\n")
def print_factor(x):
    for i in range(1, x + 1):
     if (x % i == 0): print(str(i) + " ", end="")
# your code here

l = [52633, 8137, 1024, 999]
for i in l:
    print(str(i) + " 的因子为:", end="")
    print_factor(i)
    print()
