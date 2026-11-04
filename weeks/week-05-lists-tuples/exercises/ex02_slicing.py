"""Exercise 02: slicing, mutability, alias and copy."""

numbers = [1, 2, 3, 4, 5, 6]

# TODO: create first_three and last_three using slices.
first_three: list[int] = numbers[:3]
last_three: list[int] = numbers[-3:]

# TODO: make alias refer to numbers and copied be a shallow copy.
alias: list[int] = numbers
copied: list[int] = numbers.copy()

# TODO: append through alias and explain which lists change.
alias.append(7)
# alias và numbers cùng tham chiếu một list nên cả hai thấy phần tử 7;
# copied là bản sao riêng nên không thay đổi.
print("numbers:", numbers)
print("first_three:", first_three, "last_three:", last_three)
print("alias:", alias, "copied:", copied)
