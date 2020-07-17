def soma(x,y):
    return x+y
def multiplica(x,y):
    return x*y
def divide(x,y):
    return x / y
def subtrai(x,y):
    return x - y

def test_soma():
    assert 5 == soma(2,3)
def test_multiplica():
    assert 4 == multiplica(2,2)
def test_divide():
    assert 2 == divide(10,5)
def test_subtrai():
    assert 10 == subtrai(30,20)



 
       