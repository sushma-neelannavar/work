import yaml
import sys

def sql_script_execution():
    param_file = 'param1.yaml'
    print(param_file)
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

    params['sql_script'] = sql_script

    with open(param_file, 'w') as f:
        yaml.dump(params, f)


sql_script_execution()