from threading import Thread, Lock
import time
lock = Lock()
class CreateListThread(Thread):
  def run(self):
      self.entries = []
      for i in range(10):
          time.sleep(1)
          self.entries.append(i)
      lock.acquire()
      print self.entries
      lock.release()
def use_create_list_thread():
  for i in range(2):
      t = CreateListThread()
      t.start()
  a = 1
  b = 2
  print a+b
  for i in range(2):
      t = CreateListThread()
      t.start()
  print 'hello'
  for i in range(2):
      t = CreateListThread()
      t.start()
use_create_list_thread()
