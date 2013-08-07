def obj():
    print 'Hello'

def do_n(n):
    if n <= 0:
        return
    for i in range(n):    
        obj()


do_n(3)