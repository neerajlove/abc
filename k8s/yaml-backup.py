import yaml
import redis 
import argparse
import os
import subprocess


with open(("/Users/neeraj.joshi/k8sscript/k8s/database.yaml"), "r") as filedescriptor:
    data = yaml.load(filedescriptor)
    dataentries = data.get("backup_redis")
    number = (len(dataentries))
    print("no. of database mentioned in yaml is", number)
    parser = argparse.ArgumentParser()
    for databases in dataentries:
        print(databases)
        for calc in databases:
          # here dictionary refers to keys and values in yaml  and dictionary is where i am going to get key values in form of it
          dictionary = databases[calc]
          
          # creating arguments
          parser.add_argument('-port', type=int)
          parser.add_argument('-ip', type=int)
          parser.add_argument('-password', type=str)
          parser.add_argument('-dbname', type=str)
          parser.add_argument('-filename', type=str)
          args = parser.parse_args()
          # passing args and mapping with yaml 
          args.ip = dictionary.get('host_name')
          args.dbname = dictionary.get('db_name')
          args.port = dictionary.get('db_port')
          args.password = dictionary.get('db_password')
          args.filename = dictionary.get('filename')
          
       
          # command to establish connection with redis databse 
          
          redisdata = redis.StrictRedis(host=args.ip, port=args.port, password=args.password, db=args.dbname)
          print(redisdata)
          
          # making environment variables
          os.environ['REDIS'] = args.ip
          os.environ['REDIS_PORT'] = str(args.port)
          os.environ['PASS'] = args.password
          os.environ['DBNAME'] = str(args.dbname)
          os.environ['FILENAME']= str(dictionary.get('filename'))                            
          shell = subprocess.call(["redis-dump -h $REDIS -p $REDIS_PORT -a $PASS -d $DBNAME >> $FILENAME-$(date +'%Y.%m.%d-%H.%M.%S').text"], shell=True)
          
          #print(shell)
          
          #refreshing arguments 
          parser = argparse.ArgumentParser()
        
          