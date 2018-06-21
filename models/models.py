# -*- coding: utf-8 -*-

from odoo import models, fields, api


class danh_sach_hinh_thuc(models.Model):
    _name = 'expenditure.danh_sach_hinh_thuc'
    _rec_name = 'mota'

    ten_hinh_thuc = fields.Char('Tên hình thức', required=True)
    loai_hinh_thuc = fields.Selection(selection=[('1', 'Khoản thu'), ('2', 'Khoản chi')], default='1', required=True)
    mota = fields.Char(compute='_lay_gia_tri')

    @api.multi
    @api.depends('ten_hinh_thuc', 'loai_hinh_thuc')
    def _lay_gia_tri(self):
        for rec in self:
            if rec.ten_hinh_thuc == False:
                rec.ten_hinh_thuc = 'Nope'
            if rec.loai_hinh_thuc == '1':
                rec.mota = str(rec.ten_hinh_thuc) + ' - Khoản thu'
            elif rec.loai_hinh_thuc == '2':
                rec.mota = str(rec.ten_hinh_thuc) + ' - Khoản chi'
            else:
                rec.mota = str(rec.ten_hinh_thuc) + ' - Nope'

class tai_khoan_quan_ly(models.Model):
    _name = 'expenditure.tai_khoan_quan_ly'
    _rec_name = 'user_id'

    user_id = fields.Many2one('res.users', string='Người thực hiện', default=lambda self: self.env.user)
    so_du_tai_khoan = fields.Float(string='Số dư', compute="_get_so_du_tai_khoan")
    so_khoan_thu = fields.Integer(string='Số khoản thu', store=False,readonly=True)
    so_khoan_chi = fields.Integer(string='Số khoản chi', store=False, readonly=True)
    so_khoan_no = fields.Integer(string='Số khoản nợ', store=False, readonly=True)
    so_khoan_cho_no = fields.Integer(string='Số khoản cho nợ', store=False, readonly=True)

    _sql_constraints = [
        ('user_id_unique', 'unique (user_id)', "Người dùng đã tồn tại !")
    ]


    @api.multi
    def _get_so_du_tai_khoan(self):
        for rec in self:
            list_record = rec.env['expenditure.danh_sach_thu_chi'].search([('id_tai_khoan', '=', rec.id)])
            list_record_vay_no = rec.env['expenditure.danh_sach_cac_khoan_vay'].search([('id_tai_khoan', '=', rec.id)])
            
            total = 0
            count_thu = 0
            count_chi = 0
            for data in list_record:
                if data.hinh_thuc.loai_hinh_thuc == '1':
                    total = total + data.so_tien
                    count_thu = count_thu + 1
                else:
                    total = total - data.so_tien
                    count_chi = count_chi + 1

            count_vay = 0
            count_cho_vay = 0
            for data in list_record_vay_no:
                if data.loai_hinh_thuc == '1':
                    count_vay = count_vay + 1
                    if data.da_tra == False:
                        total = total + data.so_tien
                else:
                    count_cho_vay = count_cho_vay + 1
                    if data.da_tra == False:
                        total = total + data.so_tien

            rec.so_du_tai_khoan = total
            rec.so_khoan_chi = count_chi
            rec.so_khoan_thu = count_thu
            rec.so_khoan_no = count_vay
            rec.so_khoan_cho_no = count_cho_vay


class danh_sach_cac_khoan_vay(models.Model):
    _name = 'expenditure.danh_sach_cac_khoan_vay'
    _rec_name = 'id_tai_khoan'
    _order = 'ngay_thuc_hien DESC'

    id_tai_khoan = fields.Many2one('expenditure.tai_khoan_quan_ly', string='Tài khoản' )
    so_tien = fields.Float('Số tiền')
    ngay_thuc_hien = fields.Datetime('Ngày thực hiện')
    doi_tac = fields.Char(string='Đối tác')
    nguyen_nhan = fields.Text('Nguyên nhân')
    da_tra = fields.Boolean('Đã trả', default=False)
    loai_hinh_thuc = fields.Selection(selection=[('1', 'Vay'), ('2', 'Cho vay')], string="Loại hình thức", required=True)
    hinh_anh = fields.Binary(attachment=True, string='Hình ảnh')
    hinh_anh_phu = fields.Binary(attachment=True, string='Hình ảnh phụ', required=False)
    
    # lambda self: 5

    # def print_5(self):
    #     return 5 self.id
    # @api.multi
    # def _update_so_khoan_vay(self):
    #     self.id_tai_khoan.print_5
        

    
class danh_sach_thu_chi(models.Model):
    _name = 'expenditure.danh_sach_thu_chi'
    _rec_name = 'nguyen_nhan'
    _description = 'cac khoa chi tieu ca nhan'
    _order = 'ngay_thuc_hien DESC'

    id_tai_khoan = fields.Many2one('expenditure.tai_khoan_quan_ly', string='Tài khoản')
    so_tien = fields.Float('Số tiền')
    ngay_thuc_hien = fields.Datetime('Ngày thực hiện')
    hinh_thuc = fields.Many2one('expenditure.danh_sach_hinh_thuc', 'Hình Thức', index=True, ondelete="set null")
    nguyen_nhan = fields.Text('Nguyên nhân')
    hinh_anh = fields.Binary(attachment=True, string='Hình ảnh')
    hinh_anh_phu = fields.Binary(attachment=True, string='Hình ảnh phụ', required=False)