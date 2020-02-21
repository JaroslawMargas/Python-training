from unittest import TestCase
import pytest
from lesson_03_functions import the_length_of_the_segment as lengt_seg


class TestDistance(TestCase):
    def test_distance(self):
        list_arg = [-5, -10, -5, -20]
        assert lengt_seg.distance(list_arg) == 10.0

    def test_type_test(self):
        with pytest.raises(TypeError):
            lengt_seg.distance(None, 0, 1, 1)