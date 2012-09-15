# encoding: utf-8
from google.appengine.ext import ndb
from models import Question, Answer

first_page = ndb.Key("URL", "http://www.school.kotar.co.il/KotarApp/Viewer.aspx",
                   "Params", "nBookID=95056726",
                   "Hash", "113.9392.4.fitwidth",
           )
def load():

    first_q = Question(q="איפה זה האזור הממוזג?",
                       who="קובי", 
                       parent=first_page,
              )
    first_q.put();

    Answer(parent=first_q.key,
           a="אנא עארף?",
           who="בניד",
    ).put()
    Answer(parent=first_q.key,
           a="לא יודע, אבל נשמע נעים",
           who="יוסי",
    ).put()
    second_q = Question(q="מה היה הנזק מסופת הטורנדו החזקה בהיסטוריה?", 
                        who="קובי",
                        parent=first_page,
               )
    second_q.put()
    Answer(parent=second_q.key,
           a="לא יודע",
           who="בניד",
    ).put()

