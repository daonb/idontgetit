# encoding: utf-8
import cgi
import urllib

from google.appengine.ext import ndb
import webapp2
from ndb_json import encode
# from webapp2_extras import json
from google.appengine.ext.webapp.util import run_wsgi_app

class Answer(ndb.Model):
    when = ndb.DateTimeProperty(auto_now_add=True)
    a = ndb.StringProperty()
    who  = ndb.StringProperty()

class WebPage(ndb.Model):
    url  = ndb.StringProperty()
    end_url  = ndb.StringProperty()
    title  = ndb.StringProperty()
    id  = ndb.StringProperty()

class Question(ndb.Model):
    pages = ndb.StructuredProperty(WebPage, repeated = True)
    when = ndb.DateTimeProperty(auto_now_add=True)
    q = ndb.StringProperty()
    who = ndb.StringProperty()
    answers = ndb.StructuredProperty(Answer, repeated=True)
    tag = ndb.StringProperty(repeated=True)


def load_fixture():
    tornado = WebPage(url="http://www.school.kotar.co.il/KotarApp/Viewer.aspx?nBookID=95056726#113.9392.4.fitwidth",
                end_url="http://www.school.kotar.co.il/KotarApp/Viewer.aspx?nBookID=95056726#114.1870.4.fitwidth",
                title="סופות טורנדו",
                id = "dfdfdgfbghtr64ywvrercs",)
    tornado.put()
    q1 = Question(q="איפה זה האזור הממוזג?", who="קובי", answers = [
                        Answer(a="אנא עארף?", who="בניד"),
                        Answer(a="לא יודע, אבל נשמע נעים", who="יוסי"),
                        ], pages = [tornado])
    q1.put()
    q2 = Question(q="מה היה הנזק מסופת הטורנדו החזקה בהיסטוריה?", who="קובי", answers = [
                        Answer(a="אנא עארף?", who="בניד"),
                        ], pages = [tornado])
    q2.put()

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'application/json'
    '''
    dthandler = lambda obj: obj.isoformat() if isinstance(obj,
        datetime.datetime) else str(obj) if isinstance(obj, model.BlobKey)
        else obj.id() if isinstance(obj, model.Key) else obj
    '''
    out = encode(Question.query())#, default=dthandler)

    self.response.out.write(out)

'''
class SubmitForm(webapp.RequestHandler):
  def post(self):
    # We set the parent key on each 'Greeting' to ensure each guestbook's
    # greetings are in the same entity group.
    guestbook_name = self.request.get('guestbook_name')
    greeting = Greeting(parent=ndb.Key("Book", guestbook_name or "*notitle*"),
                        content = self.request.get('content'))
    greeting.put()
    self.redirect('/?' + urllib.urlencode({'guestbook_name': guestbook_name}))
'''


load_fixture()
application = webapp2.WSGIApplication([
  ('/', MainPage),
])
# ('/sign', SubmitForm)

