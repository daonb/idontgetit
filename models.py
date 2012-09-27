from google.appengine.ext import ndb
class CommonModel(ndb.Model):
    who = ndb.StringProperty()
    when = ndb.DateTimeProperty(auto_now_add=True)

class Page(ndb.Model):
    url = ndb.StringProperty()

class Answer(CommonModel):
    a = ndb.StringProperty()

class Question(CommonModel):
    q = ndb.StringProperty()
    tag = ndb.StringProperty(repeated=True)
    page = ndb.KeyProperty()
    answers = ndb.StructuredProperty(Answer, repeated=True)

