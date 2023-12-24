import types

failed_conditions = []


def check(assert_condition, message=None):
    global failed_conditions
    if isinstance(assert_condition, types.FunctionType):
        try:
            assert_condition()
        except AssertionError as error:
            add_exception(message if message else error)
    else:
        try:
            assert assert_condition
        except AssertionError:
            add_exception(message if message else 'Failed by assertion!')


def add_exception(message=None):
    global failed_conditions
    failed_conditions.append(f'Failure: {message}\n')


def verify_expectations():
    global failed_conditions
    if failed_conditions:
        report = ['Failed conditions count: [ {} ]\n'.format(len(failed_conditions))]
        for index, failure in enumerate(failed_conditions, start=1):
            if len(failed_conditions) > 1:
                report.append(f'{index}. {failure}')
            else:
                report.append(failure)
        failed_conditions = []
        raise AssertionError('\n'.join(report))


class verify:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        verify_expectations()
