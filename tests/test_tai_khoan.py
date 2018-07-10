from odoo.tests.common import TransactionCase

class AccountTestCase(TransactionCase):
    def setUp(self):
        super(AccountTestCase, self).setUp()
        book_model = self.env['expenditure.danh_sach_hinh_thuc']
        self.book = book_model.create({
            'ten_hinh_thuc': 'Test hinh thuc',
            'loai_hinh_thuc': 'ho moi',
        })
    
    def test_change_draft_available(self):
        '''test changing state from draft to available'''
        self.book.ten_hinh_thuc = 'abc'
        self.assertEqual(self.book.ten_hinh_thuc, 'abc')