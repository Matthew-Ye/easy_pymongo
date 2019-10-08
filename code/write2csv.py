import codecs
import csv
import pymongo

#build connection
conn = pymongo.MongoClient('127.0.0.1',27017)
#connect dataBase
mydb = conn.test
#get collection
tripCollect = mydb.testCollect


#查询库中数据
cursor = my_collection.find()
#打开csv文件
with codecs.open('../data/output.csv', 'w', 'utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # # 先写入columns_name
    # writer.writerow(["name", "content", "topic", "at"])
    # #写入多行用writerows
    # for data in cursor:
    #     writer.writerows([[data["name"], data["content"], data["topic"], data["at"]]])