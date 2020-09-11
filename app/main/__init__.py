from flask import Blueprint
main = Blueprint('main',__name__)
# from . import views,errors
try:
  from . import views,errors
except:
  pass