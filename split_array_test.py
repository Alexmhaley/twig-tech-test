import pytest
import random

from split_array import split_array


class TestSplitArray():

    def test_given_list(self):
        test_array = [1,2,3,4,5]
        step = 3
        output = split_array(test_array, step)
        assert output == [[1,2], [3,4], [5]]
        assert len(output) == step

    def test_even_list(self):
        test_array = [1,2,3,4]
        step = 4
        output = split_array(test_array, step)
        assert output == [[1], [2], [3], [4]]
        assert len(output) == step

    def test_one_list(self):
        test_array = [1,2,3,4]
        step = 1
        output = split_array(test_array, step)
        assert output == [test_array]
        assert len(output) == step

    def test_negative_step(self):
        test_array = [1,2,3,4]
        step = -1
        output = split_array(test_array, step)
        assert not output
        assert len(output) == 0

    def test_empty_array(self):
        test_array = []
        step = 3
        output = split_array(test_array, step)
        assert output == test_array
        assert len(output) == 0
