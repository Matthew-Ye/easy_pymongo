import pymongo
import csv
from datetime import datetime

 
#build connection
conn = pymongo.MongoClient('127.0.0.1',27017)
#connect dataBase
mydb = conn.test
#get collection
tripCollect = mydb.testCollect
#get data



# csvfile = file('../data/2018_Yellow_Taxi_Trip_Data.csv','rb')
# VendorID,
# tpep_pickup_datetime,
# tpep_dropoff_datetime,
# passenger_count,
# trip_distance,
# RatecodeID,
# store_and_fwd_flag,
# PULocationID,
# DOLocationID,
# payment_type,
# fare_amount,
# extra,
# mta_tax,
# tip_amount,
# tolls_amount,
# improvement_surcharge,
# total_amount
# 2,
# 11/04/2084 12:32:24 PM,
# 11/04/2084 12:47:41 PM,
# 1,
# 1.34,
# 1,
# N,
# 238,
# 236,
# 2,
# 10,
# 0,
# 0.5,
# 0,
# 0,
# 0.3,
# 10.8
# with open(input_text) as file:
#      csvfile = file.read().decode('utf-8', 'replace')

with open('../data/2018_Yellow_Taxi_Trip_Data.csv',''r'',encoding=''utf-8'')as csvfile:
	reader=csv.DictReader(csvfile)
	counts=0
    for each in reader:
        # 将数据中需要转换类型的数据转换类型。原本全是字符串（string）。
        each['VendorID']=int(each['VendorID'])
        each['tpep_pickup_datetime']=datetime.strptime(each['tpep_pickup_datetime'], '%m/%d/%y %I:%M:%S %p')
        each['tpep_dropoff_datetime']=datetime.strptime(each['tpep_dropoff_datetime'], '%m/%d/%y %I:%M:%S %p')
        each['passenger_count']=int(each['passenger_count'])
        each['trip_distance']=float(each['trip_distance'])
        each['RatecodeID']=int(each['RatecodeID'])
        # each['store_and_fwd_flag']=String(each['store_and_fwd_flag'])
        each['PULocationID']=int(each['PULocationID'])
        each['DOLocationID']=int(each['DOLocationID'])
        each['payment_type']=int(each['payment_type'])
        each['fare_amount']=float(each['fare_amount'])
        each['extra']=float(each['extra'])
        each['mta_tax']=float(each['mta_tax'])
        each['tip_amount']=float(each['tip_amount'])
        each['tolls_amount']=float(each['tolls_amount'])
        each['improvement_surcharge']=float(each['improvement_surcharge'])

        tripCollect.insert(each)
        counts+=1
        print('insert '+str(counts)+' data')


#csv_reader = csv.reader(csvfile)
csv_reader = csv.DictReader(csvfile)
#get time befor writing
print (datetime.datetime.now())
for i in range(3,103):
    for row in csv_reader:
        #print data, for test
        #print row    
        print(row['deviceId'])
        # print(row['deviceId'])
        # row['VendorID'] = int(row['VendorID'])
        tripCollect.insert(row)
#get time after writing
print (datetime.datetime.now())
csvfile.close()


# Delete all records in the collection
def deleteCollection (collection):
	collection.delete_many({})
	return collection



# ID = 'firstRecord'
# insertDate = '2017-08-28'
# count = 10
# insert_record = {'_id':ID, 'endDate': insertDate, 'count': count}

# deviceId='1'

def insertone (insert_record):
	insert_res = db_coll.insert_one(insert_record)
	print(f"insert_id={insert_res.inserted_id}: {insert_record}")
	return insert_res.deviceId


# ordered = True，遇到错误 break, 并且抛出异常
# ordered = False，遇到错误 continue, 循环结束后抛出异常
insertRecords = [{'i':i, 'date':'2017-10-10'} for i in range(10)]

def insertmany (insertRecords, order=True):
	insertBulk = db_coll.insert_many(insertRecords, ordered)
	print(f"insert_ids={insertBulk.deviceId}")
	return
