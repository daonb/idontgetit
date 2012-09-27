# encoding: utf-8
import jinja2
import os
import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app

from models import Question, Answer
import fixture

jinja_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
  def get(self):
    context = []
    qs =  Question.query()
    # import pdb; pdb.set_trace()
    # qs.map_async(lambda x: context.append())

    temp = jinja_env.get_template('templates/popup.html')
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


fixture.load()
application = webapp2.WSGIApplication([
  ('/', MainPage),
])
# ('/sign', SubmitForm)

