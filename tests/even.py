def even_number(n):
    return n %2 ==0

def test_even_number():
   for n in range(20,200):
       if n %2 == 0:
           assert even_number(n) == True
       else:
           assert even_number(n) == False