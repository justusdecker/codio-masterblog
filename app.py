from flask import Flask
from flask import render_template, request

from bin.blog import Blog, BlogPost

app = Flask(__name__)




BLOG = Blog()
@app.route('/')
def index():
    return render_template('index.html', posts=BLOG.asclass())

@app.route('/add', methods=['GET', 'POST'])
def add():
    post_flag = False
    if request.method == 'POST':
        new_post = {"id": BLOG.length+1,
         "author":request.form['author'],
         "title": request.form['title'],
         "content": request.form['content']}
        BLOG.add(BlogPost(new_post))
        post_flag = True
        
        
    return render_template('add.html',post_flag=post_flag)

@app.route('/delete/<int:post_id>')
def delete(post_id):
    if not BLOG.aslist():
        return "Blog does not exist", 404
    BLOG.delete(post_id)
    return render_template('index.html')


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    # Fetch the blog posts from the JSON file
    if post_id >= BLOG.length or post_id is None:
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