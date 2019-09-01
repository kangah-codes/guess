from google.appengine.ext import ndb

class Number(ndb.Model):
    score = ndb.IntegerProperty(required=True)
