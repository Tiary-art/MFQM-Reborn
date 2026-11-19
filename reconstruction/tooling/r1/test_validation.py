import io
import json
import unittest
import zipfile
from validate import assert_models, unique, declared_creative

class ValidationTests(unittest.TestCase):
    def test_duplicate_stack(self):
        with self.assertRaises(ValueError):unique([('WaxWood',4),('WaxWood',4)])
    def models(self, docs):
        stream=io.BytesIO()
        with zipfile.ZipFile(stream,'w') as z:
            for name,doc in docs.items():
                z.writestr('assets/mfqm/models/item/'+name+'.json',json.dumps(doc))
        with zipfile.ZipFile(stream) as z:return assert_models(z)
    def test_missing_model(self):
        with self.assertRaisesRegex(ValueError,'missing model'):
            self.models({'wax':{'parent':'mfqm:item/absent'}})
    def test_parent_cycle(self):
        with self.assertRaisesRegex(ValueError,'parent cycle'):
            self.models({'a':{'parent':'mfqm:item/b'},'b':{'parent':'mfqm:item/a'}})
    def test_numbered_name_is_not_creative_output(self):
        self.assertEqual(set(declared_creative('BlockBrownClay')),{0,4})
        self.assertEqual(set(declared_creative('BlockWaxWood')),{0,4})
    def test_int_signature_creative_candidate(self):
        self.assertEqual(set(declared_creative('BlockMorass')),set(range(1,9)))
if __name__=='__main__':unittest.main()
