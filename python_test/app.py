# Example with the class
from flask import Flask
import time
from threading import Thread
from socketIO_client import SocketIO, LoggingNamespace
app = Flask(__name__)


class InitiateApp(object):
  def __init__(self):
    self.socketIO = SocketIO('127.0.0.1', 8000, LoggingNamespace)
    self.socketIO.on('connect', self.on_connect)
    self.socketIO.on('disconnect', self.on_disconnect)
    self.socketIO.on('reconnect', self.on_reconnect)
    self.socketIO.on('chat message', self.on_message)
    self.receive_events_thread = Thread(target=self.move_to_thread)
    self.receive_events_thread.daemon = True
    self.receive_events_thread.start()

  def on_connect(self):
    print('connect')
    self.socketIO.emit('join', 'room2')

  def on_disconnect(self):
    print('disconnect')

  def on_reconnect(self):
    print('reconnect')
    self.socketIO.emit('join', 'room2')

  def on_message(self, *args):
    print('on chat message', args)

  def move_to_thread(self):
    self.socketIO.wait()


def main():
  InitiateApp()

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == "__main__":
  main()
  app.run(port=5490)
