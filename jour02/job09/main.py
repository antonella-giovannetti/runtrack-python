def Triangle(a, b, c):
    maximum = max(a, b ,c)
    if 2*maximum <=  a + b + c: 
        if a == b == c:
            print('triangle équilatéral')
        elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
            print('triangle rectangle')         
        elif a == b or a == c or b == c:
            print('triangle isocèle')
        elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a and a == b or a == c or b == c:
            print('triangle rectangle isocèle')
        else:
            print('triangle quelconque')
    else:
        print('Il est impossible de construire un triangle')


Triangle(8, 5, 4)