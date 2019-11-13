# Example without the class

from flask import Flask
import time
from threading import Thread
from socketIO_client import SocketIO, LoggingNamespace
app = Flask(__name__)

def on_connect():
  print('connect')
  socketIO.emit('join', 'room1')

def on_disconnect():
  print('disconnect')

def on_reconnect():
  print('reconnect')

def move_to_thread():
  global socketIO
  socketIO.wait()

def main():
  global socketIO
  socketIO = SocketIO('127.0.0.1', 8000)
  socketIO.on('connect', on_connect)
  socketIO.on('disconnect', on_disconnect)
  socketIO.on('reconnect', on_reconnect)
  receive_events_thread = Thread(target=move_to_thread)
  receive_events_thread.daemon = True
  receive_events_thread.start()

if __name__ == "__main__":
  main()
  app.run()

