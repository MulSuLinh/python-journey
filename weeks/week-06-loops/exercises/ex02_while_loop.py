"""Exercise 02: while, break and continue."""

remaining = 5

# TODO: count down to 1 and update remaining on every pass.
while remaining > 0:
    print(remaining)
    remaining -= 1
print("Bắt đầu!")

# TODO: loop through 1..10, skip multiples of 3 and stop after 8.
number = 0
while number < 10:
    number += 1
    if number > 8:
        break
    if number % 3 == 0:
        continue
    print(number)

print(remaining)
