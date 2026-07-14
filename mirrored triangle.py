rows = 5 # You can change this number for different sizes

for i in range(1, rows + 1):
    # Print spaces first to push the stars to the right
    print(" " * (rows - i) + "*" * i)