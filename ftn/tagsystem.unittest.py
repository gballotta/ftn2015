__author__ = 'Giovanni'


import unittest
from tagsystem import FtnTagInterface, FtnTag

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.tagger = FtnTagInterface()
    def test_addtag(self):
        self.tagger.addTag("pinco")
        self.tagger.addTag("pallo")
        self.tagger.addTag("pinco")
        riscontro = ["pinco", "pallo"]
        self.assertEqual(self.tagger.tags, riscontro)

    def test_secondo(self):
        self.tagger.tags = ["pinco", "diotallevi", "bulbo"]
        self.tagger.delTag("diotallevi")
        self.tagger.delTag("casaubon")
        self.assertEqual(self.tagger.tags, ["pinco", "bulbo"])

    def test_hastag_true(self):
        self.tagger.tags = ["pinco", "diotallevi", "bulbo"]
        self.assertTrue(self.tagger.hasTag("diotallevi"))

    def test_hastag_false(self):
        self.tagger.tags = ["pinco", "diotallevi", "bulbo"]
        self.assertFalse(self.tagger.hasTag("casaubon"))


class MaxTestCase(unittest.TestCase):
    def setUp(self):
        self.tagger = FtnTag("pippo")

    def test_creazionestringa(self):
        self.tagger.tags = ["passala", "gamba", "spiridione"]
        self.assertEqual(self.tagger.formatTags(), "ftntag = passala,gamba,spiridione")

if __name__ == '__main__':
    unittest.main()
