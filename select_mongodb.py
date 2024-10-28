from pymongo import MongoClient

# MongoDB에 연결
client = MongoClient("mongodb://172.17.0.3:27017/")  # my_mongodb는 Docker 컨테이너 이름입니다
db = client.mydatabase  # 데이터베이스 이름
collection = db.data_collection  # 컬렉션 이름

# 컬렉션의 모든 문서를 조회
documents = collection.find()
count = 0
# 조회한 문서 출력
for doc in documents:
    print(doc)
    count += 1

print(count)
