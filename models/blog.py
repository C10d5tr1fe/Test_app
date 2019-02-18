import uuid


class Blog():

    #конструктор
    def __init__(self, title, description, author, id = None):
        self.title = title
        self.description = description
        self.author = author
        self.blog_id = uuid.uuid4().hex if id is None else id

    def new_post(self):
       pass

    def get_post(self):
       pass

    #запись в базу данных блога
    def save_to_mongo(self):
        Database.insert(collection = 'blog', data = self.json())

    #json блога
    def json(self):
        return {
            #'id':self.id,
            'blog_id':self.blog_id,
            'author':self.author,
            'content':self.content,
            'title':self.title,
            #'created_date':self.create_date
        }