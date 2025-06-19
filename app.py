from flask import Flask
from flask import render_template, request

from json import load, dumps

app = Flask(__name__)

def jff(path: str) -> list | dict:
    """ returns a json file """
    with open(path,'r') as f_in:
        return load(f_in)

def jsf(path: str, data: dict | list) -> None:
    """ write json to a file """
    with open(path,'w') as f_out:
        f_out.write(dumps(data,indent=2))

class BlogPost:
    def __init__(self, data):
        self.data = data
    
    def asdict(self) -> dict:
        return {
            'title': self.title,
            'author': self.author,
            'content': self.content
        }
    
    @property
    def title(self) -> str:
        return self.data['title']
    @property
    def author(self) -> str:
        return self.data['author']
    @property
    def content(self) -> str:
        return self.data['content']

class Blog:
    def __init__(self):
        self.load()
    
    def save(self):
        jsf('blog.json',self.aslist())
    
    def load(self):
        self.data = [BlogPost(i) for i in jff('blog.json')]
    
    def aslist(self) -> list:
        return [i.asdict() for i in self.data]
    
    def add(self, post: BlogPost) -> None:
        self.data.insert(0,post)
    
    def delete(self, post_id: int) -> None:
        self.data.pop(post_id)
    
    @property
    def length(self) -> int:
        return len(self.data)

BLOG = Blog()
@app.route('/')
def index():
    overwrite = ""
    
    return render_template('index.html', posts=blog_posts).replace('__BLOG_POSTS__', overwrite)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_post = {"id": BLOG.length+1,
         "author":request.form['name'],
         "title": request.form['title'],
         "content": request.form['content']}
        BLOG.add(BlogPost(new_post))
        
    return render_template('add.html')

@app.route('/delete/<int:post_id>')
def delete(post_id):
    BLOG.delete(post_id)
    return render_template('index.html')


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    # Fetch the blog posts from the JSON file
    if post_id >= BLOG.length:
        return 'cant find post', 404
    if post_id < 0:
        return 'negative type not supported', 404
    if request.method == 'POST':
        # Update the post in the JSON file
        # Redirect back to index
        request
    # Else, it's a GET request
    # So display the update.html page
    return render_template('update.html', post=BLOG)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)