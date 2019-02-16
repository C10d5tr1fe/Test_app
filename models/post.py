from models.database import Database
import datetime


class Post(object):

    def __init__(self, blog_id,  title, content, date=datetime.datetime.utcnow(), author, id):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.id = id
        self.create_date = date

    def save_to_mongo(self):
        Database.insert(collection = 'post', data = self.json())

    def json(self):
        return {
            'id':self.id,
            'blog_id':self.blog_id,
            'author':self.author,
            'content':self.content,
            'title':self.title,
            'created_date':self.create_date
        }

    @staticmethod
    def from_mongo(id):
        #Post.from_mongo('123')
        return Database.find_one(collection='posts', query={'id':id})

    @staticmethod
    def from_blog(id):
        return [ post for post in Database.find(collection = 'post', query={'blog_id':id})]





