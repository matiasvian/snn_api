import unittest
from SNN_logic import SNN
import requests

class TestSNNLogic(unittest.TestCase):

    def setUp(self):
        snns = ['10029940539', '31129956715']
        self.snn = SNN(snns=snns)

    def test_valid(self):
        self.assertTrue(self.snn.valid('10029940539'))
    
    def test_invalid(self):
        self.assertFalse(self.snn.valid('1002994053'))
        self.assertFalse(self.snn.valid('10029940539a'))
        self.assertFalse(self.snn.valid('10029940B39 '))
        self.assertFalse(self.snn.valid('400299540539'))
        self.assertFalse(self.snn.valid('-10929940539'))
        self.assertFalse(self.snn.valid(10029940539))

    def test_man(self):
        self.assertEqual(self.snn.gender('10029940539'), 'Man')
    
    def test_woman(self):
        self.assertEqual(self.snn.gender('08015314495'), 'Woman')
    
    def test_age(self):
        self.assertEqual(self.snn.age('10029940539'), 23)
        self.assertEqual(self.snn.age('31129956715'), 123)

    def test_is_among_given_snns(self):
        self.assertTrue(self.snn.is_among_given_snns('10029940539'))
        self.assertFalse(self.snn.is_among_given_snns('10028940539'))

    def test_count_by_gender(self):

        self.assertEqual(self.snn.count_by_gender(), {'man': 2})

    def test_count_by_gender_by_age(self):

        self.assertEqual(self.snn.count_by_gender_by_age(), {'man': {23: 1, 123: 1}, 'woman': {}})

class TestSNNApi(unittest.TestCase):

    def test_api(self):
        response = requests.get('http://0.0.0.0:8000/')
        self.assertEqual(response.status_code, 200)
        
    def test_valid(self):
        response = requests.get('http://0.0.0.0:8000/valid?snn=10029940539')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'true')
    
    def test_invalid(self):
        response = requests.get('http://0.0.0.0:8000/valid?snn=1002994053')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'false')    
    
    def test_gender(self):
        response = requests.get('http://0.0.0.0:8000/gender?snn=10029940539')
        self.assertEqual(response.status_code, 200)

    def test_age(self):
        response = requests.get('http://0.0.0.0:8000/age?snn=10029940539')
        self.assertEqual(response.status_code, 200)
    
    def test_is_among_given_snns(self):
        response = requests.get('http://0.0.0.0:8000/is_among_given_snns?snn=10029940539')
        self.assertEqual(response.status_code, 200)
    
    def test_count_by_gender(self):
        response = requests.get('http://0.0.0.0:8000/count_by_gender')
        self.assertEqual(response.status_code, 200)

    def test_count_by_gender_by_age(self):
        response = requests.get('http://0.0.0.0:8000/count_by_gender_by_age')
        self.assertEqual(response.status_code, 200)

def main():
    unittest.main()

if __name__ == '__main__':
    unittest.main()


