# Koch Curve exercise
# Name: Aarthi Narayan
from TurtleWorld import * 		

world = TurtleWorld()			
bob = Turtle()				
bob.delay = 0.05

#Was successfull in creating the koch curve all by myself in around 2 hours. 
def koch(t,length):
	
	if length < 3 :
		fd(t,length)
		return

	angle = 60
	koch(t,length/3.0)	
	lt(t,angle)
	koch(t,length/3.0)
	lt(t, -2*angle)
	koch(t,length/3.0)
	lt(t,angle)
	koch(t,length/3.0)

def snowflake(t,length):
	for i in range(3):
		koch(t,length)
#While trying to do the snowflake, I struggled for a long time as I did not comprehend
#that to form the snoflake outline the curve would need a right tilt of 120 degrees. This is where I peeked at the
#solution.		
		rt(t, 120)


snowflake(bob,600)


wait_for_user()