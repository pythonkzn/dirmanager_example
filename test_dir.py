import unittest
import unittest
import unittest.mock
from mock import patch
import dir_manager
import json


with open('fixtures/documents.json', 'r', encoding='utf8') as out_docs:
    documents = json.load(out_docs)


class TestDir(unittest.TestCase):
    def test_list(self):
        list1 = dir_manager.show_document_info(documents[0])
        self.assertEqual(list1, 'passport "2207 876234" "Василий Гупкин"')

    def test_add(self):
        dir_manager.append_doc_to_shelf('1', '1')
        self.assertEqual(dir_manager.directories['1'][-1], '1')

    @unittest.mock.patch('builtins.input', side_effect=['10006'])
    def test_del(self, mock):
        dir_manager.delete_doc()
        self.assertEqual(len(dir_manager.documents), 2)

    @unittest.mock.patch('builtins.input', side_effect=['11-2'])
    def test_get_shelf(self, mock):
        self.assertEqual(dir_manager.get_doc_shelf(), '1')

if __name__ == '__main__':
    unittest.main()

