from soft_assert import check, verify


class TestPytestExample():

    def test_positive(self):
        with verify():
            check('one' == 'one')
            check(3 == 3, 'Custom message if test failed')
            check([0, 1] == [0, 1])
            check(1 == 1)

    def test_negative(self):
        with verify():
            check('one' == 'two')
            check('one' == 'two', 'one != two')
            check(1 == 2)
            check(2 == 3, 'Custom message if test failed')
            check([6, 7] == [8, 9], 'Lists not equals')

    def test_mixed(self):
        with verify():
            check(1 == 1)
            check(2 == 3, 'Custom message if test failed')
            check([0, 1] == [0, 1])
            check([6, 7] == [8, 9], 'Lists not equals')
            check('one' == 'one')
            check('one' == 'two', 'one != two')


    def test_loop_example(self):
        with verify():
            for number in range(1, 10):
                check(number % 2 == 0, f'{number} is not divisible by 2 without remainder!')

    def test_one_condition(self):
        check(1 > 3, '1 < 3')
