import yaml
import sys

def sql_script_execution(param_file):
    #param_file = 'param.yaml'
    #print(param_file)
    with open(param_file, 'r') as f:
        params = yaml.load(f, Loader=yaml.FullLoader)
        print(type(params))
    #print(params['start_date'])
    #print(params['end_date'])
    #print(params['state'])
    start_date = params['start_date']
    end_date = params['end_date']
    state = params['state']
    mode = params['mode']
    sql_script = "SELECT * FROM Transaction WHERE CREATED BETWEEN " + start_date + " AND " + end_date + " AND State = " + state + " AND Mode = " + mode
    #print(sql_script)
    print("SQL script constructed successfully")
    
    
    #params['sql_script'] = sql_script

#def write_file(params)
    with open('updated_dates.yaml', 'r') as fs:
        upd_parm = yaml.load(fs, Loader=yaml.FullLoader)
    
    upd_parm['start_date'] = start_date
    upd_parm['end_date'] = end_date

    with open('updated_dates.yaml', 'w') as fh:
        yaml.dump(upd_parm, fh)
    
    #print('substituted value')
    #return "SQL script constructed successfully"

if __name__ == "__main__":
    param_file = sys.argv[1]
    sql_script_execution(param_file)