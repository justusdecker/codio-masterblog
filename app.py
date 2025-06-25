from flask import Flask
from flask import render_template, request, redirect

from bin.blog import Blog, BlogPost

app = Flask(__name__)

BLOG = Blog()


@app.route('/')
def index():
    """
    Renders the main index page of the blog application.

    This function fetches all blog posts from the `BLOG` object and passes
    them to the 'index.html' template for rendering.
    """
    return render_template('index.html', posts=BLOG.asclass())

@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Handles the addition of new blog posts.

    This function responds to both GET and POST requests:
    - **GET request:** Renders the 'add.html' template, displaying a form
      for users to input new blog post details. The `post_flag` is initially
      set to False, indicating no post has been added yet.
    - **POST request:** Processes the submitted form data. It extracts the
      author, title, and content from the request form, creates a new
      `BlogPost` object. The `id` for the new post is determined by
      `BLOG.get_highest_index()`.
      This new post is then added to the `BLOG` collection, and `post_flag`
      is set to True to indicate a successful post submission.

    Finally, it renders the 'add.html' template, passing the `post_flag`
    to potentially display a success message or modify the form's appearance.
    """
    post_flag = False
    if request.method == 'POST':
        new_post = {
         "author":request.form['author'],
         "title": request.form['title'],
         "content": request.form['content'],
         "id": BLOG.get_highest_index()}
        BLOG.add(BlogPost(new_post))
        post_flag = True
    return render_template('add.html',post_flag=post_flag)

@app.route('/delete/<int:post_id>')
def delete(post_id):
    """
    Deletes a specific blog post based on its ID.

    This function handles the deletion of a blog post identified by `post_id`.
    It first performs several checks to ensure the `post_id` is valid:
    - If `post_id` is greater than or equal to the total number of blog posts (`BLOG.length`).
    - If `post_id` is None (though Flask's int converter usually prevents this for routes).
    - If there are no blog posts currently loaded (`not BLOG.aslist()`).
    
    If any of these conditions are met, it returns a 404 error, indicating
    that the specified blog post does not exist or the blog is empty.
    Otherwise, it attempts to delete the post using `BLOG.delete(post_id)`.
    After successful deletion, it renders the main index page.
    """
    print(BLOG.aslist())
    if not BLOG.get_post_by_id(post_id):
        return "Blog does not exist", 404
    BLOG.delete(post_id)
    return redirect('/')


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    # Fetch the blog posts from the JSON file
    if BLOG.get_post_by_id(post_id) is None:
        return "Blog does not exist", 404
    if post_id < 0:
        return 'negative post_id not supported', 404
    if request.method == 'POST':
        # Update the post in the JSON file
        # Redirect back to index
        BLOG.update(post_id,request.form['author'],request.form['title'],request.form['content'])
    # Else, it's a GET request
    # So display the update.html page
    return render_template('update.html', post=BLOG.get_post_by_id(post_id))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)