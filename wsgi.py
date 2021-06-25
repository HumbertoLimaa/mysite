from flask_app import app as application
import sys
path = '/home/humbertolimaa/mysite'
if path not in sys.path:
    sys.path.insert(0, path)
