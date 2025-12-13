n = int(input("Enter your amount: "))
coins = [len("Vika"), len("Parfyonova"), len("Vadimovna")]
flag = 0

for a in range(n // coins[0] + 1):
    for b in range(n // coins[1] + 1):
        for c in range(n // coins[2] + 1):
            if n - (coins[0] * a + coins[1] * b + coins[2] * c) == 0:
                flag = 1
                break
        if flag:
            break
    if flag:
        break

if flag == 0:
    print("-42!")
else:
    print(f"{a} coins of {coins[0]}")
    print(f"{b} coins of {coins[1]}")
    print(f"{c} coins of {coins[2]}")
