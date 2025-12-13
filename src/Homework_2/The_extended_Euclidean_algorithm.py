def extended_gcd(a, b):
    old_remainder, remainder = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while remainder != 0:
        quotient = old_remainder // remainder
        old_remainder, remainder = remainder, old_remainder - quotient * remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return f"Decomposition of Bezu: {a}*{old_s} \
        + {b}*{old_t} = {old_remainder}"


a, b = map(int, input("Enter 'a' and 'b' separated by a space: ").split())

print(extended_gcd(a, b))
