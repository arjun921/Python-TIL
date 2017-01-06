def is_leap(year):
    leap = False
    
    # Write your logic here
    if n%4==0:
        leap = True
        if n%100==0:
            leap = False
            if n%400==0:
                leap = True
    else:
        leap = False
    return leap

year = int(input())
print(is_leap(year))
