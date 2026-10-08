# d_flip_flop.py

print("================================")
print("       D FLIP-FLOP SIMULATOR")
print("================================")

Q = 0

while True:
    print("\nCurrent Q =", Q)

    D = int(input("Enter D (0 or 1): "))
    CLK = int(input("Enter Clock (0 or 1): "))

    if D not in [0, 1] or CLK not in [0, 1]:
        print("Invalid input! Enter only 0 or 1.")
        continue

    if CLK == 1:
        Q = D
        print("Clock is HIGH")
        print("Next State Q =", Q)
    else:
        print("Clock is LOW")
        print("Q remains =", Q)

    choice = input("\nDo you want to continue? (y/n): ")

    if choice.lower() != 'y':
        print("\nSimulation completed.")
        break
