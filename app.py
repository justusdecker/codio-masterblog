from flask import Flask
from flask import render_template, request

from json import load

app = Flask(__name__)

def jff(path: str) -> list | dict:
    """ returns a json file """
    with open(path,'r') as f_in:
        return load(f_in)

class BlogPost:
    def __init__(self, data):
        self.data = data
    @property
    def title(self) -> str:
        return self.data['title']
    @property
    def author(self) -> str:
        return self.data['author']
    @property
    def content(self) -> str:
        return self.data['content']

blog_posts = [BlogPost(i) for i in jff('blog.json')]
@app.route('/')
def index():
    overwrite = ""
    for blog_post in blog_posts:
        overwrite += f"""
<div class="post">
    <h2>{blog_post.title}</h2>
    <p><em>{blog_post.author}</em></p>
    <p>{blog_post.content}</p>
</div>

        """
    return render_template('index.html', posts=blog_posts).replace('__BLOG_POSTS__', overwrite)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # We will fill this in the next step
        new_post = {"id": len(blog_posts)+1,
         "author":request.form['name'],
         "title": request.form['title'],
         "content": request.form['content']}
        blog_posts.append(new_post)
        
        
    return render_template('add.html')

@app.route('/delete/<int:post_id>')
def delete(post_id):
    blog_posts.pop(post_id)
    return render_template('index.html', posts=blog_posts)


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    # Fetch the blog posts from the JSON file
    post = blog_posts.index()
    if post is None:
        # Post not found
        return "Post not found", 404
    
    if request.method == 'POST':
        # Update the post in the JSON file
        # Redirect back to index
        request
    # Else, it's a GET request
    # So display the update.html page
    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)