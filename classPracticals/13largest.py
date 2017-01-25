def max_in_list(ls):
    largest = ls[0]
    for x in ls:
        if x>largest:
            largest = x
    return largest

ls = [2,5,7,2,3,7,9,2,251]
print(max_in_list(ls))
