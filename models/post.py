from models.database import Database

class Post(object):

    def __init__(self, blog_id,  title, content, date, author, id):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.id = id
        self.create_date = date

    def save_to_mongo(self):
        Database.insert(collections = 'post', data = self.json())

    def json(self):
        return {
            'id':self.id,
            'blog_id':self.blog_id,
            'author':self.author,
            'content':self.content,
            'title':self.title,
            'created_date':self.create_date
        }



