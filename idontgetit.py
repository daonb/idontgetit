# encoding: utf-8
import jinja2
import os
from google.appengine.ext import ndb
import webapp2
from ndb_json import encode
# from webapp2_extras import json
from google.appengine.ext.webapp.util import run_wsgi_app

jinja_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Answer(ndb.Model):
    when = ndb.DateTimeProperty(auto_now_add=True)
    a = ndb.StringProperty()
    who  = ndb.StringProperty()

class WebPage(ndb.Model):
    url  = ndb.StringProperty()
    end_url  = ndb.StringProperty()
    title  = ndb.StringProperty()

class Question(ndb.Model):
    when = ndb.DateTimeProperty(auto_now_add=True)
    q = ndb.StringProperty()
    who = ndb.StringProperty()
    tag = ndb.StringProperty(repeated=True)
    answers = ndb.StructuredProperty(Answer, repeated=True)
    pages = ndb.StructuredProperty(WebPage, repeated = True)


def load_fixture():
    tornado = WebPage(url="http://www.school.kotar.co.il/KotarApp/Viewer.aspx?nBookID=95056726#113.9392.4.fitwidth",
                end_url="http://www.school.kotar.co.il/KotarApp/Viewer.aspx?nBookID=95056726#114.1870.4.fitwidth",
                title="סופות טורנדו",
                )
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
    temp = jinja_env.get_template('popup.html')
    # self.response.out.write(temp.render([a.to_dict for a in Question.query()]))
    qs = []
    for q in Question.query():
        answers = []
        for a in q.answers:
            answers.append({"a": a.a, "who": a.who})

        qs.append({"q": q.q, "who": q.who,
            "answers": answers,
            })

    self.response.out.write(temp.render({"qs": qs}))
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

