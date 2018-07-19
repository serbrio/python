import sys
num_steps = int(sys.argv[1])

for n in range(num_steps):
    print((" "*(num_steps-(n+1))) + ("#"*(n+1)))

