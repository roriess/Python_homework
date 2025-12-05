def reverse_lexicographical_compare(string_1, string_2):
    return True if string_1 >= string_2 else False


string_1 = input()
string_2 = input()
print(reverse_lexicographical_compare(string_1, string_2))
