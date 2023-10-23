import pytest
import sys
from temp2 import sql_script_execution

#@pytest.mark.parametrize(param_file)

#@pytest.fixture(scope='session', autouse=False)
#def input_val():
#    return "param1.yaml"

def test_sql(request):
    myarg_value = request.config.getoption("--name")
    print("success")
    result = sql_script_execution(myarg_value)
    assert result == "SQL script constructed successfully"
