# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    shape = ""
    if n >= 1:
        for i in range(n):
            shape += "*"
        shape += "\n"
    for i in range(n - 2):
        shape += "*"
        for i in range(n - 2):
            shape += " "
        shape += "*\n"
    if n > 1:
        for i in range(n):
            shape += "*"
    return shape.rstrip()
   
# 1
# 12
# 123
# 1234
def number_pattern(n):
    shape = ""
    i = 1

    while i <= n:
        j = 1
        line = ""

        while j <= i:
            line += str(j)
            j += 1

        shape += line + "\n"
        i += 1

    return shape.rstrip()

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0 
    i = 1

    while i <= n:
        total += i
        i += 1

    return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    shape = ""
    i = 1

    while i <= n:
        spaces_count = n - i
        j = 0 
        while j < spaces_count:
            shape += " "
            j += 1

        stars_count = 2 * i - 1
        k = 0
        while k < stars_count:
            shape += "*"
            k += 1

        if i < n:
            shape += "\n"
        i += 1

    return shape