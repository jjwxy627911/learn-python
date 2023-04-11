def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

# Sample use
print(avg(1, 2)) #  # 1.5
print(avg(1, 2, 3, 4)) # 2.5