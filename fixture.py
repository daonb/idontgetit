# encoding: utf-8
from google.appengine.ext import ndb
from models import Question, Answer, Page

def load():
    first_page = Page(url="http://www.example.com")
    first_page_key = first_page.put()

    first_q = Question(q="איפה זה האזור הממוזג?",
                       who="קובי", 
                       page=first_page_key,
                       answers = [Answer(a="אנא עארף?",
                                         who="בניד"),
                                  Answer(a="לא יודע, אבל נשמע נעים",
                                         who="יוסי",
                                        ),
                                 ],
                      ).put_async()

    second_q = Question(q="מה היה הנזק מסופת הטורנדו החזקה בהיסטוריה?", 
                        who="קובי",
                        page=first_page_key,
                        answers = [Answer(a="לא יודע",
                                          who="בניד",
                                         ),
                                  ],
                        ).put_async()
