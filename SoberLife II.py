import sys
import os
from Sober_Life_II.__main__ import main

# if getattr(sys, 'frozen', False):
#     os.chdir(os.path.dirname(sys.executable))

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

if __name__ == '__main__':
    main()
