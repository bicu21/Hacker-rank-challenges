# 
def is_leap(year):
    leap = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
   
    
    return leap

year = int(input())
print(is_leap(year))

def is_leap(year):
    leap = False

    if year % 4 == 0:
        print(True)
    elif year % 100 == 0:
        print(False)
    elif year % 400 == 0:
        print(True)
    
    return leap
year = int(input())
print(is_leap(year))
