from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# insert / find / update / delete 

# insert 예시 -----------------------------------------------------
doc = {'name':'jane','age':21}
db.users.insert_one(doc)

# find 예시 -------------------------------------------------------
same_ages = list(db.users.find({'age':21},{'_id':False}))   # {'_id':False} : _id 값은 제외하고 출력
for person in same_ages:
    print(person['name'], person['age'])

all = list(db.users.find({},{'_id':False}))                 # 모든 document를 find 해!
print(all)

user = db.users.find_one({'name':'bobby'},{'_id':False})    # find_one : 하나만 가져올 때
print('user: ', user)

# update 예시 -----------------------------------------------------
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})   # 조건에 일치하는 가장 상단의 1명의 age만 변경
db.users.update_many({'name':'bobby'},{'$set':{'age':33}})  # bobby라는 이름을 가진 모든 age를 변경 (잘 쓰지는 안음)

# delete 예시 -----------------------------------------------------
db.users.delete_one({'name':'bobby'})
db.users.delete_many({'name':'jane'})