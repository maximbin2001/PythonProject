from math import sqrt
TRIANGLE_SIDES_LIST = [20,10,5,10,3,10]

storona = 0
s_max = -1
for i in range(len(TRIANGLE_SIDES_LIST)):
    for k in range(i+1,len(TRIANGLE_SIDES_LIST)):
        for j in range(k+1,len(TRIANGLE_SIDES_LIST)):
            a  = TRIANGLE_SIDES_LIST[i]
            b = TRIANGLE_SIDES_LIST[k]
            c = TRIANGLE_SIDES_LIST[j]
            if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0:
                p = (a + b + c) / 2
                s = sqrt(p * (p - a) * (p - b) * (p - c))
                if s > s_max:
                    s_max = s


print(s_max)

