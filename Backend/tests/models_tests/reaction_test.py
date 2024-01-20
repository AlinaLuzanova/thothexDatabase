import unittest
from src.models.reaction import Reaction


class TestReaction(unittest.TestCase):

    def test_to_dict(self):
        name = "amide formation"
        reaction = Reaction(name)

        expected = {"name": name}
        actual = reaction.to_dict()

        self.assertEqual(expected, actual)
