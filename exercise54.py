# This is where Exercise 5.4 goes
# Name: Aarthi Narayan

def is_triangle(a,b,c):
	if c >= a + b or a >= b + c or b >= c + a:
	    print "No"
	else:
	    print "Yes"
	       
def integer_input():
	a = raw_input('What is the first length?\n')
	int(a)
        b = raw_input('What is the second length?\n')
        int(b)
	c = raw_input('What is the third length?\n')
	int(c)
	is_triangle(a,b,c)

integer_input()