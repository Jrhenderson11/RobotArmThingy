import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# Windows and Linux
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
# Mac
#arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
import socket
import math

class SampleListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        print "Frame available"
        frame = controller.frame()
       
        hands = frame.hands
        hand = hands[0]
    
        grab = float(hand.grab_strength)
        x = hand.palm_position.x
        y = hand.palm_position.y
        z = hand.palm_position.z
        rX = math.floor(x)		
        rY = math.floor(y)	
        rZ = math.floor(z)	
        
        print rX
        print rY
        print rZ
        data = str(int(rX)) + ':' + str(int(rY)) + ':' + str(int(rZ)) + ':'+str(grab) 
        if len(hands)>0:
        	send(data)
        else:
        	#send default coords
			send('0:150:0:0.5')
			
				        
class Connection():
	
	def __init__(self):
		self.s = socket.socket()         
		self.host = socket.gethostname() 
		self.port = 12345 
		self.connected = False
	
	def start_server(self):
		s = self.s
		s.bind(('192.168.10.3', self.port))
		s.listen(5)
		print 'listening'
		self.c, addr = s.accept()
		self.connected = True
		print 'Got connection from', addr
			
	def is_connected(self):
		return self.connected
		
	def send(self, data):
		self.c.send(data)
	
	def close(self):
		self.c.close()   


global server
server = Connection()
	
def main():

	listener = SampleListener()

	controller = Leap.Controller()
	# got leap
	

	server.start_server()
	
	controller.add_listener(listener)
	print 'listener started'	
		        
	# Keep this process running until Enter is pressed
	print "Press Enter to quit..."
	try:
	    sys.stdin.readline()
	except KeyboardInterrupt:
	    pass
	finally:
	    controller.remove_listener(listener)
	send('close')
	server.close()

def is_connected():
	return server.is_connected()

def send(data):
	server.send(data)

if __name__ == "__main__":
	main()
