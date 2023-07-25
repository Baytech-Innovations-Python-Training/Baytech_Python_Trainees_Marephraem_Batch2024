n=52525
def find_reverse(val):
    rem = val
    reverse = 0
    for i in range(len(list(str(val)))):
        digit = rem % 10
        reverse = reverse*10 + digit
        rem = rem // 10
    return reverse
def find_palindrome():
    reverse = find_reverse(val=n)
    if n == reverse:
        return True
    else:
        return False

res = find_palindrome()

if res:
    print(f'{n} is palindrome')
else:
    print(f'{n} is not palindrome')