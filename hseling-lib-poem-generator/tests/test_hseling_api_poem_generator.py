import unittest

import hseling_api_poem_generator


class HSELing_API_Poem_generatorTestCase(unittest.TestCase):

    def setUp(self):
        self.app = hseling_api_poem_generator.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to hseling_api_Poem Generator', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
