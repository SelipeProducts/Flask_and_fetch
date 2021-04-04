from . import db
from sqlalchemy.sql import func

class Notes(db.Model):
  id = db.collumn(db.Integer, primary_key=True)
  data = db.collumn(db.String(10000))
  date1 = db.collumn(db.DateTime(timezone=True, defualt = func.now))
  
