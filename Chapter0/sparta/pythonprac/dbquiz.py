from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# quiz 1 - 영화제목 '매트릭스'의 평점을 가져오기
score = db.movies.find_one({'title':'매트릭스'})['star']
print(score)

# quiz 2 - '매트릭스'의 평점과 같은 평점의 영화 제목들을 가져오기
same_movies = list(db.movies.find({'star':score}))
for movie in same_movies:
    print(movie['title'])

# quiz 3 - 매트릭스 영화의 평점을 0으로 만들기
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})