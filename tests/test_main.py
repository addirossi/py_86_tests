from unittest import TestCase, skipIf, expectedFailure

from main import summarize, get_dict, NUMBER, get_list, factorial


class TestSomething(TestCase):
    def test_ok(self):
        a = 10
        b = 20
        expected = 30
        result = summarize(a, b)
        self.assertEqual(result, expected)

    def test_failed(self):
        a = 10
        b = 15
        result = summarize(a, b)
        # result > 30
        self.assertGreater(result, 30)

    def test_error(self):
        a = 20
        b = '25'
        result = summarize(a, b)
        expected = 45
        self.assertEqual(result, expected)

    def test_regex(self):
        date1 = '1999-09-11'
        date2 = '09.11.2023'
        date3 = '09/11/2023'

        pattern = '\d{2}\.\d{2}\.\d{4}'
        # self.assertRegex(date1, pattern)
        self.assertRegex(date2, pattern)
        self.assertNotRegex(date3, pattern)

    @skipIf(NUMBER > 40, 'Too big value')
    def test_key_in_dict(self):
        key = 'a'
        dict1 = get_dict()
        self.assertIn(key, dict1)

    @expectedFailure
    def test_expected_failure(self):
        a = 10
        list1 = get_list()
        self.assertIn(a, list1)


import pytest


class TestSomethingWithPytest:
    @pytest.mark.xfail
    def test_equal(self):
        a = 10
        b = 20
        result = summarize(a, b)
        expected = 30
        assert result == expected


def test_failure():
    a = 10
    b = 20
    result = summarize(a, b)
    assert result > 35


@pytest.mark.skipif(NUMBER > 40, reason='Too big value')
def test_key_in_dict():
    key = 'a'
    dict1 = get_dict()
    assert key in dict1


@pytest.mark.xfail
def test_expected_failure():
    a = 10
    list1 = get_list()
    assert a in list1


@pytest.mark.parametrize(
    'number,expected', (
        [1, 1],
        [5, 120],
        [6, 720],
        [10, 3628800]
    )
)
def test_factorial(number, expected):
    result = factorial(number)
    assert result == expected

