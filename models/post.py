from models.database import Database
import datetime


class Post(object):

    #конструктор поста
    def __init__(self, blog_id,  title, content, author,  date = datetime.datetime.utcnow(), id = None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.id = id
        self.create_date = date

    #запись в базу данных поста
    def save_to_mongo(self):
        Database.insert(collection = 'post', data = self.json())

    #json поста
    def json(self):
        return {
            'id':self.id,
            'blog_id':self.blog_id,
            'author':self.author,
            'content':self.content,
            'title':self.title,
            'created_date':self.create_date
        }

    #метод поиска поста в бд
    @classmethod
    def from_mongo(cls, id):
        #Post.from_mongo('123')
        post_data = Database.find_one(collection='posts', query={'id':id})
        return cls( blog_id = post_data['blog_id'],
                    title = post_data['title'],
                    content = post_data['content'],
                    author = post_data['author'],
                    date = post_data['created_data'],
                    id = post_data['id'])

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection = 'post', query={'blog_id':id})]





