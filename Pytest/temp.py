import yaml
import sys
#from pyspark.sql import SparkSession

#start_date = sys.argv[1]
#end_date = sys.argv[2]
#spark = SparkSession.builder.master("local[1]").appName("SparkExamples.com").getOrCreate()

def sql_script_execution(param_file):
    with open(param_file, 'r') as f:
        params = yaml.load(f, Loader=yaml.FullLoader)

    #print(params['start_date'])
    #print(params['end_date'])
    #print(params['state'])
    start_date = params['start_date']
    end_date = params['end_date']
    state = params['state']
    mode = params['mode']
    sql_script = "SELECT * FROM Transaction WHERE CREATED BETWEEN " + start_date + " AND " + end_date + " AND State = " + state + " AND Mode = " + mode
    print(sql_script)
    print("SQL script constructed successfully")
    return "SQL script constructed successfully"


    #spark.sql(sql_script)
if __name__ == "__main__":
    #param_file = sys.argv[1]
    sql_script_execution(param_file)


