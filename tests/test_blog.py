import pytest
from bin.blog import Blog, BlogPost, IndexDuplicateError

def test_create():
    Blog()
def test_load_duplicate_id():
    BLOG = Blog()
    with pytest.raises(IndexDuplicateError):
        BP = BlogPost(
            {
                'id': 1,
                'author': "justus",
                'title': "pytest",
                "content": "cheese"}
        )
        BLOG.add(BP)
def test_load():
    BLOG = Blog()
    
    BP = BlogPost(
        {
            'id': 4,
            'author': "justus",
            'title': "pytest",
            "content": "cheese"}
    )
    BLOG.add(BP)