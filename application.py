import json
from flask import Flask, jsonify
application = Flask(__name__)

from markupsafe import escape

def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

header_text = '''
    <html>\n<head> <title>ElasticBeanstalk Flask App with CodePipeline!</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: Welcome! This is a simple Flask app. 
    If you append a username to the URL like this: 
    <code>/fernando</code> to say hello to someone specific
    it will give them a nice  greeting .</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

@application.route('/user/<user_id>')
def get_user_profile(user_id):
    with open('data.json', 'r') as f:
        data = json.load(f)
        result = next(item for item in data if item["id"] == escape(user_id))
    return jsonify(result)

if __name__ == "__main__":
    application.debug = True
    application.run()
