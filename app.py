from models.database import Database
from models.post import Post

Database.initialize()


post = Post("Post 1 title", "Post 1 content", "Post one author")
post2 = Post("Post 1 title", "Post 1 content", "Post one author")


print(post.title)
print(post2.content)





print(12)







"""import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['local']
collection = database['students']

students = [student['name'] for student in collection.find({})]  #list comprehentions

print(students)
"""
