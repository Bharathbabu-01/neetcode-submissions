def check_range(num: int) -> str:
    if num < 0:
        return str("negative")
    elif num == 0:
        return str("zero")
    elif (num > 0) & (num < 10):
        return str("positive single digit")
    elif num >= 10:
        return str("positive multi digit")
  
# don't modify code below this line
print(check_range(-10))
print(check_range(0))
print(check_range(9))
print(check_range(100))
