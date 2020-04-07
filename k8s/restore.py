import json 
import redis
import os
import subprocess
import yaml

with open(("/Users/neeraj.joshi/k8sscript/k8s/database.yaml"), "r") as filedescriptor:
    data = yaml.load(filedescriptor)
    dataentries = data.get("backup_redis")
    number = (len(dataentries))
    print("no. of database mentioned in yaml is", number)
  
    for databases in dataentries:
        print(databases)
        for check in databases:
             read = databases[check]
             os.environ['REDISPASS'] = str(read.get('db_password'))
             os.environ['PORT'] = str(read.get('db_port'))
             os.environ['REDIS'] = read.get('host_name')
             os.environ['REDISFILE'] = str(read.get('filename'))
                
             shell = subprocess.call(["cat $REDISFILE | redis-cli -h $REDIS -p $PORT -a $REDISPASS" ], shell=True)
             print(shell)