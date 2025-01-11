def sum_recurs(n):
    if n ==1 or n==0:
        return 1
    return n + sum_recurs(n-1)
a=25
x= sum_recurs(a)
print(" THE SUM OF FIRST {a} NATURAL NUMBER IS {X} ")