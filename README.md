[![PyPI version](https://badge.fury.io/py/soft-asserts.svg)](https://badge.fury.io/py/soft-asserts)
[![Downloads](https://pepy.tech/badge/soft-asserts)](https://pepy.tech/project/soft-asserts)
# soft-asserts
Soft assertions for Python/Pytest

## Installation

```bash
    pip install soft-asserts
```
## Usage

Assertion is performed immediately after the call `check()`, 
but the expected result is obtained only after exit the context manager `verify()`

Quick example:
```python
    from  soft_asserts import check, verify

    def test_something():
        with verify():
            check(1 == 1)
            check(2 > 1, 'Message if test failed')
            check('one' != 'two', 'Some message')
```

You can use asserts in loop:
```python
    from  soft_asserts import check, verify
    
    def test_asserts_in_loop():
        with verify():
            for number in range(1, 10):
                check(number % 2 == 0, '{number} is not a multiple of 2')
```

Also you can use it with pytest parametrized tests:
```python
    import pytest
    from  soft_asserts import check, verify

    @pytest.mark.parametrize('number', list(range(1, 10)))
    def test_pytest_example(number):
        with verify():
            check(number % 2 == 0)
```

Example of output:
```python
    AssertionError: Failed conditions count: [ 4 ]
    
    1. Failure: Custom message if test failed
    
    2. Failure: Lists not equals
    
    3. Failure: Your custom message; 4 < 5!
    
    4. Failure: one != two
```

More examples you can find in `test_example.py` 
