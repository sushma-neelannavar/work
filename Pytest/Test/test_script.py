import pytest
import sys
from temp2 import sql_script_execution

#@pytest.mark.parametrize(param_file)

@pytest.fixture
def input_val():
    return "param1.yaml"

def test_sql(input_val):
    print("success")
    result = sql_script_execution(input_val)
    assert result == "SQL script constructed successfully"
