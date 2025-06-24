from bin.datamanagement import jsf,jff

class BlogPost:
    """
    Represents a single blog post, providing access to its title, author,
    content, and a unique identifier.

    This class encapsulates the data for a blog post and provides methods
    to access this data, primarily through properties and a method to
    convert the post to a dictionary.
    """
    def __init__(self, data):
        """Initializes a BlogPost instance with the provided data."""
        self.data = data
    
    def asdict(self) -> dict:
        """Converts the BlogPost object into a dictionary representation."""
        return {
            'title': self.title,
            'author': self.author,
            'content': self.content,
            'id': self.id
        }
    @property
    def id(self) -> str:
        """Gets the unique identifier of the blog post."""
        return self.data['id']
    @property
    def title(self) -> str:
        """Gets the title of the blog post."""
        return self.data['title']
    @property
    def author(self) -> str:
        """Gets the author of the blog post."""
        return self.data['author']
    @property
    def content(self) -> str:
        """Gets the content of the blog post."""
        return self.data['content']
    
class Blog:
    """
    Manages a collection of blog posts, providing methods for loading, saving,
    adding, and deleting posts.

    This class interacts with a 'blog.json' file to persist blog post data.
    Each blog post is expected to be an instance of a 'BlogPost' class
    """
    def __init__(self):
        """
        Initializes the Blog instance and loads existing blog posts from
        'blog.json'.
        """
        self.load()
    
    def save(self):
        """
        Saves the current list of blog posts to 'blog.json'.
        It converts each BlogPost object into a dictionary before saving.
        """
        jsf('blog.json',self.aslist())
    
    def load(self):
        """
        Loads blog posts from 'blog.json' into the 'data' attribute.
        Each loaded post is converted into a BlogPost object.
        """
        self.data = [BlogPost({i}) for i in jff('blog.json')]
        print(self.aslist())
    
    def aslist(self) -> list:
        """Converts the list of BlogPost objects into a list of dictionaries."""
        return [i.asdict() for i in self.data]
    
    def asclass(self) -> list:
        """Returns the raw list of BlogPost objects."""
        return [i for i in self.data]
    
    def add(self, post: BlogPost) -> None:
        """Adds a new blog post to the beginning of the list."""
        self.data.insert(0,post)
    
    def delete(self, post_id: int) -> None:
        """Deletes a blog post by its index (ID)."""
        self.data.pop(post_id)
    def get_highest_index(self) -> int:
        """this will prevent most of the duplicate id issues"""
        return max([i.id for i in self.data])
    
    @property
    def length(self) -> int:
        """Gets the number of blog posts currently in the blog."""
        return len(self.data)