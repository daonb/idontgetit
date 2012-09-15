from google.appengine.ext import ndb
class CommonModel(ndb.Model):
    tag = ndb.StringProperty(repeated=True)
    who = ndb.StringProperty()
    when = ndb.DateTimeProperty(auto_now_add=True)

class Answer(CommonModel):
    a = ndb.StringProperty()

class Question(CommonModel):
    q = ndb.StringProperty()

    @property
    def answers(self):
        return Answer.query(ancestor=self.key)

