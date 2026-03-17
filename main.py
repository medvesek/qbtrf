import sys
import os
import traceback
from src.setup import setup
from src.add import addTorrent
from src.lib.config import configExists 

try:
  if len(sys.argv) == 1 or not configExists():
    setup()

  elif len(sys.argv) > 1:
    addTorrent(sys.argv[1])

  print("Great success!")
except Exception as e:
  print("Oh no. Something went wrong.")
  traceback.print_exc()
  input("...")