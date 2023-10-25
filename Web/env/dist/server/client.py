from settings import *
from client_window import Window
from network import Network

window = Window()

while not window.done:
    window.connect()
    
n = Network(window.host, window.port)

while window.running and not n.closed:
    window.run()
    if window.down == 1:
        n.send('1')
    else:
        n.send('0')