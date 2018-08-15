from google.appengine.api import users
from google.appengine.ext import ndb
import webapp2
import jinja2
import os
from PIL import Image 

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('./main.html')
        self.response.out.write(template.render())

    def Read(self):
        print(image.info)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
