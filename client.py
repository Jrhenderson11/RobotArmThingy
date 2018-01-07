import socket               # Import socket module
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinList = [2, 3, 4, 5, 6]

for i in pinList: 

	GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.LOW)

#setup 

power1 = 2
power2 = 3

base = 5
arm = 4
claw = 6

s = socket.socket()         
host = socket.gethostname()
port = 12345                

s.connect(('192.168.10.3', port))
data = 'asd'

grabbing = 1

while (data != 'close'):
	data = s.recv(1024)
	print data
	xa,ya,za,g = data.split(':')
#	print x
#	print y
#	print z
#	print 'grab: ' + str(grab)
	grab = float(g)
	x =  int(xa)
	y = float(ya)
	z = float(za)
	
	if grab >= 0.9 and grabbing != 2:
		print grab
		print 'grabbing'
		GPIO.output(2, GPIO.HIGH)
        	GPIO.output(3, GPIO.HIGH)
		GPIO.output(claw, GPIO.HIGH)		
		grabbing = 2
	if grab <= 0.07 and grabbing !=0:
		print 'opening'
		GPIO.output(2, GPIO.LOW)
	        GPIO.output(3, GPIO.LOW)
                GPIO.output(claw, GPIO.HIGH)
		grabbing = 0
	elif (grab < 0.9 and grab > 0.07) and (grabbing !=1):
		print 'stopping'
		GPIO.output(claw, GPIO.LOW)
		grabbing = 1
	
	if y >= 180 :
                print 'raising'
                GPIO.output(2, GPIO.LOW)
                GPIO.output(3, GPIO.LOW)
                GPIO.output(arm, GPIO.HIGH)
                
        elif y <= 110 :
                print 'lowering'
                GPIO.output(2, GPIO.HIGH)
                GPIO.output(3, GPIO.HIGH)
                GPIO.output(arm, GPIO.HIGH)
                
        else:
                print 'stopping arm'
                GPIO.output(arm, GPIO.LOW)
               

	
GPIO.output(claw, GPIO.LOW)
GPIO.output(base, GPIO.LOW)
GPIO.output(arm, GPIO.LOW)

s.close()
GPIO.cleanup()



