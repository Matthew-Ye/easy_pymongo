import pymongo
import csv
from datetime import datetime

FILEPATH='../data/test.csv'

def build_connection():
	#build connection
	conn = pymongo.MongoClient('127.0.0.1',27017)
	#connect dataBase
	mydb = conn.test
	#get collection
	tripCollect = mydb.testCollect
	return

def load_from_csv(FILEPATH):
	with open(FILEPATH,'r',encoding='utf-8')as csvfile:
    reader=csv.DictReader(csvfile)
    counts=0
    for each in reader:
        each['VendorID']=int(each['VendorID'])
        each['tpep_pickup_datetime']=datetime.strptime(each['tpep_pickup_datetime'], '%m/%d/%Y %I:%M:%S %p')
        each['tpep_dropoff_datetime']=datetime.strptime(each['tpep_dropoff_datetime'], '%m/%d/%Y %I:%M:%S %p')
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

        tripCollect.insert_one(each)
        counts+=1
    print('insert '+str(counts)+' data')
