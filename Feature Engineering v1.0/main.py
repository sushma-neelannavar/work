from pyspark import SparkContext,SparkConf 
from pyspark.sql import SparkSession, HiveContext
from pyspark.sql import functions as F
from pyspark.sql.functions import col
from pyspark.sql.functions import substring,to_date,date_sub,when,add_months,expr,row_number,col,lit,concat,current_date,current_timestamp,lit
import sys
import logging
import argparse
from datetime import datetime
import yaml
import os
import time

#############################################-spark configuration-######################################################
conf = SparkConf()
conf.set("hive.vectorized.execution","true")
conf.set("hive.vectorized.execution.enabled","true")
conf.set("hive.cbo.enable","true")
conf.set("hive.compute.query.using.stats","true")
conf.set("hive.stats.fetch.column.stats","true")
conf.set("hive.stats.fetch.partition.stats","true")
conf.set("spark.dynamicAllocation.enabled","true")
conf.set("spark.io.compression.codec","snappy")
conf.set("spark.ui.enabled","false")
conf.set("spark.ui.port","4070")
conf.set("spark.serializer","org.apache.spark.serializer.KryoSerializer")
conf.set("spark.sql.shuffle.partitions","150")

# global dictionary
dates_dict = {}

class FeatureStore:
    def __init__(self, config_file_path,hive_load_date,back_fill_month):
        try:
            logging.info("Reading config file path")
            self.config_file_path = config_file_path
            self.hive_load_date = hive_load_date
            self.back_fill_month = back_fill_month
            self.config = None
            self.spark = None
            print("config_file_path:", config_file_path)
            print("hive_load_date:", hive_load_date)
            logging.info("Config file read!")
        except Exception as e:
            logging.error("Error in reading config file path")
            logging.error(e)
    
    def load_yml(self):
        try:
            logging.info("Loading yaml file")

            #loading common_property.yml file
            current_directory = os.getcwd()
            print(current_directory)
            #common_property_location = current_directory + "\common_property.yml"
            #print(common_property_location)

            self.config_file_path = self.config_file_path
            print(self.config_file_path)
            
            #with open(common_property_location, 'r') as file:
            #    common = yaml.safe_load(file)
            #print(common['SourceSinkConfiguration']['sourceyaml'])
            #self.config_file_path = common['SourceSinkConfiguration']['sourceyaml'] + self.config_file_path
            

            #loading yml that contains features queries 
            with open(self.config_file_path, 'r') as file:
                self.config = yaml.safe_load(file)
                #print(self.config)
                print("Yaml file read")
            logging.info("Yaml file read!")

        except Exception as e:
            logging.error("Error in loading yaml file")
            logging.error(e)

    ''' def create_spark_seesion(self):
        self.spark = SparkSession       \
        .builder                        \
        .appName(self.config['featureEngineering']['featureComputeLogic']['logicFor'])\
        .config(conf = conf)            \
        .enableHiveSupport()            \
        .getOrCreate()
        self.spark.sql('set mapred.output.compression,codec = org.apache.hadoop.io.compress.SnappyCodec')
        self.spark.sql('set mapred.output.compression.type = BLOCK')
        self.spark.sql('set hive.exec.dynamic.partition.mode = nonstrict')
        self.spark.sql('set hive.exec.dynamic,partition = true')
        self.spark.sql('set spark.sql.autoBroadcastJoinThreshold = 1')
        self.spark.sql('set spark.sql.crossJoin.enable = true') '''


    def process_queries(self):
        try:
            logging.info("Reading of sql query names from yaml file satrted!")
            print("Reading of sql query names from yaml file satrted!")
            
            #print(self.config['featureEngineering']['feature_logic'])
            for query in self.config['featureEngineering']['feature_logic']:
                #print(query)
                feature = query['featurename']
                #print("Features: ", feature)
                #print(feature)
                flag = query['status']
                print("Flag: ", flag)
                if(flag == 1):
                    sql_queries = query['queries']
                    #print(sql_queries)
                    for q in sql_queries:
                        #print(q)
                        name = q['name']
                        #print("Name:", name)                        
                        print("name:", q['name'])                        
                        print("sql:", q['sql'])
                        print("\n")

                        '''if(q['param']==1):
                            parm_sql_query = q['sql']
                            parameterized_query = param_sql_query.format(date = self.hive_load_date, month = self.back_fill_month)
                            print(parameterized_query)
                            #sql_df = self.spark.sql(parameterized_query)
                            #sql_df.createOrReplaceRempView(q['name'])
                            print(q['name'], parameterized_query)

                        else:
                            
                            #sql_df = self.spark.sql(q['sql'])
                            #sql_df.createOrReplaceTempView(q['name'])
                            print(q['name'],q['sql'])
                        '''

        except Exception as e:
            logging.error("Reading of sql names from yaml files failed!")
            logging.error(e)

    # new function to read and store dates 
    def update_dates(self):
        global dates_dict
        try:
            logging.info("Reading of sql query for date extraction from yaml file started!")
            for query in self.config['featureEngineering']['feature_dates']:
                print('Yaml read')
                #print(query)
                sql_queries = query['queries']
                for q in sql_queries:
                    name = q['name']
                    sql_query = q['sql']
                    dates_dict[name] = sql_query
            print(dates_dict)

            file=open("updated_dates.yaml","w")
            yaml.dump(dates_dict,file)
            file.close()
            print("YAML file saved.")

        except Exception as e:
            logging.error("Reading of sql query for dates from yaml files failed!")
            logging.error(e)


    def target_query(self):
        write_query = self.config['featureEngineering']['featureStore']['writeLogic']
        print("Write_Query: ", write_query)
        #df = self.spark.sql(write_query)
        sink = self.config['featureEngineering']['featureStore']
        print("Sink Details: ", sink)
        #df.show() 
        #df.write.insertInto(sink['database'] + '.' + sink['table'], True)

        #df = df.select('*', current_timestamp().alias('created_on'))
        #df.write.mode(sink['write_mode']).saveAsTable(sink['database'] + '.' + sink['featureTable'])
        #row_count = df.count()
        #print("Number or rows in the Dataframe:", row_count) 
        #df.show()
        #print("Printing final dataframe schema")
        #df.printSchema()

    # def test(self):
    #   print("file path", self.config_file_path)
    #   print("hive_load_Date from function", self.hive_load_date)

start_time = time.time()
parser = argparse.ArgumentParser()
parser.add_argument('--params', nargs = '*', help= 'Extra arguments to pass to the job')
args = parser.parse_args()
print("Called with arguments: {}".format(args))
job_args = dict()
if args.params:
    job_args_tuples = [arg_str.split('=') for arg_str in args.params]
    print("job_args_tuples: {}".format(job_args_tuples))
    job_args ={a[0]: a[1] for a in job_args_tuples}
config_file_path = job_args['config_file']
hive_load_date = job_args['hive_load_date']
back_fill_month = job_args['back_fill_month']
obj = FeatureStore(config_file_path, hive_load_date, back_fill_month)
obj.load_yml()
# obj.test()

#obj.create_spark_session()
obj.update_dates()
obj.process_queries()
obj.target_query()
end_time = time.time()
elapsed_time = (end_time - start_time)
print("time taken to execute whole spark code", elapsed_time)
print("hive_load_date", hive_load_date)
