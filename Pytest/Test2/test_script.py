import pytest
import sys
from temp2 import sql_script_execution

#@pytest.mark.parametrize(param_file)

#@pytest.fixture
#def input_val():
#    return "param1.yaml"

def test_sql(request):
    print("success")
    myarg = request.config.getoption("--name")
    result = sql_script_execution(myarg)
    assert result == "SQL script constructed successfully"
