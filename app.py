from flask import Flask

app = Flask(__name__)
from flask import render_template
from json import load

def jff(path: str) -> list | dict:
    """ returns a json file """
    with open(path,'r') as f_in:
        return load(f_in)
blog_posts = jff('blog.json')
@app.route('/')
def index():
    # add code here to fetch the job posts from a file
    return render_template('index.html', posts=blog_posts)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)