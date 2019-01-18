import pymongo
from bson.objectid import ObjectId
# 连接MongoDB
client = pymongo.MongoClient(host='localhost',port=27017)
# 连接text数据库
db = client.text
# 连接数据库中的集合(collection),类似于关系型数据库中的表
collection = db.students
# 查找所有students表中所有的数据，返回的是一个生成器对象
results = collection.find()
print(type(results))
for result in results:
    print(result)
results = collection.find().sort('name',pymongo.DESCENDING).skip(2).limit(1)
print('***********************************')
result = collection.find({'_id':ObjectId('5c39b5554708832e400014d3')})
print(type(result))
print(result)
print('*'*20)
data = {
    'id':{'$gt':0}
}
result = collection.delete_many()
print(type(result))
print(result)
for i in collection.find():
    print(i)





