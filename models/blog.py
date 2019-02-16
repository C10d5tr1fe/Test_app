from pymongo.database import Database
from models.post import Post
import datetime

class Blog():

    def __init__(self, author, title, description, id = None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date = input("Enter date or leave blank for today (in format DDMMYYYY): ")
        post = Post( blog_id = self.id,
                     title = title,
                     content = content,
                     date = datetime.datetime.strptime(date, "%d%m%Y"),
                     author=self.author )
        post.save_to_mongo()



    def get_post(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection = 'blogs', data = self.json())

    def json(self):
        return {
                 'author':self.author,
                 'title':self.title,
                 'description':self.description,
                 'id':self.id
               }

    @staticmethod
    def get_from_mongo(id):
        blog_data = Database.find_one(collection = 'blogs',
                                      query = {'id' : id} )
        return  Blog(
                      author = blog_data['author'],
                      title = blog_data['title'],
                      description= blog_data['description'],
                      id = blog_data['id']
                    )



