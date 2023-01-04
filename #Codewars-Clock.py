#Codewars-Clock
def past(h, m, s):
    h=h*3600000
    m=m*60000
    s=s*1000
    total = h+m+s
    return total

print(str(past(1,0,0)))