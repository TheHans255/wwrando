#!/usr/bin/python3.11

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

import sys

sys.path.insert(0, "./gclib")

from collections import OrderedDict

from wwr_ui.randomizer_window import WWRandomizerWindow

def signal_handler(sig, frame):
  print("Interrupt")
  sys.exit(0)

# Allow keyboard interrupts on the command line to instantly close the program.
import signal
signal.signal(signal.SIGINT, signal_handler)

try:
  from sys import _MEIPASS # @IgnoreException
except ImportError:
  # Setting the app user model ID is necessary for Windows to display a custom taskbar icon when running the randomizer from source.
  import ctypes
  app_id = "LagoLunatic.WindWakerRandomizer"
  try:
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
  except AttributeError:
    # Versions of Windows before Windows 7 don't support SetCurrentProcessExplicitAppUserModelID, so just swallow the error.
    pass

cmd_line_args = OrderedDict()
for arg in sys.argv[1:]:
  arg_parts = arg.split("=", 1)
  if len(arg_parts) == 1:
    cmd_line_args[arg_parts[0]] = None
  else:
    cmd_line_args[arg_parts[0]] = arg_parts[1]

qApp = QApplication(sys.argv)

# Have a timer updated frequently so keyboard interrupts always work.
# 499 milliseconds seems to be the maximum value that works here, but use 100 to be safe.
timer = QTimer()
timer.start(100)
timer.timeout.connect(lambda: None)

window = WWRandomizerWindow(cmd_line_args=cmd_line_args)
sys.exit(qApp.exec())
