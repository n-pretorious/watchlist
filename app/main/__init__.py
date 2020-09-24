from flask import Blueprint
main = Blueprint('main',__name__)

try:
  from . import views,errors
except:
  pass