

import pytest

if __name__ == '__main__':
    pytest.main(['-vs', 'test_case', '--reruns', '3', '--alluredir', './allure_data'])