# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.osv import expression

class sales_search(models.Model):
    _inherit = "sale.order.line"

    category_saerch = fields.Many2one('product.category', "Category")
    category_saerch_setting = fields.Boolean("Category" ,related="company_id.category_search")

    
    @api.onchange('category_saerch')
    def get_company_sale_setting(self):
        saerch_setting = self.env.company.category_search
        if  saerch_setting == True:
            for rec in self:
                 rec.product_id=False
                 rec.name=""
                 return {'domain': {'product_id': [('categ_id', '=', rec.category_saerch.id)]}}
        else:         
                 return {'domain': {'product_id': [('sale_ok', '=', True), '|', ('company_id', '=', False), ('company_id', '=', saerch_setting)]}}    

class purchase_search(models.Model):
    _inherit = "purchase.order.line"

    category_saerch = fields.Many2one('product.category', "Category")
    category_saerch_setting = fields.Boolean("Category" ,related="company_id.category_search")

    
    @api.onchange('category_saerch')
    def get_company_sale_setting(self):
        saerch_setting = self.env.company.category_search
        if  saerch_setting == True:
            for rec in self:
                 rec.product_id=False
                 rec.name=""
                 return {'domain': {'product_id': [('categ_id', '=', rec.category_saerch.id)]}}
        else:         
                 return {'domain': {'product_id': [('sale_ok', '=', True), '|', ('company_id', '=', False), ('company_id', '=', saerch_setting)]}}    


    #product_id = fields.Many2one(
    #    'product.product', string='Product', domain=lambda self: self._get_categ_id(),
    #    change_default=True, ondelete='restrict', check_company=True)
    #
    #def _get_categ_id(self):
    #    category_id =self.category_saerch
    #    domain = [('sale_ok', '=', True), ('company_id', '=', False),('company_id', '=', self.company_id),('categ_id', '=', category_id)]
    #    print(domain)
    #    return domain
    


class ProductTemplate(models.Model):
    _inherit = "product.product"

    #@api.model
    #def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
    #    args = args or []
    #    domain = []
    #    if self.env.company.category_search == True:
    #        if str(args[0])=="['sale_ok', '=', True]" or str(args[0])=="['purchase_ok', '=', True]":
    #            if name:
    #             domain = ['|', '|', ('name', operator, name), ('default_code', operator, name),
    #                  '|', ('barcode', operator, name), ('categ_id', operator, name)] 
    #        else:
    #            if name:
    #             domain = ['|', '|', ('name', operator, name), ('default_code', operator, name),
    #                  '|', ('barcode', operator, name), ('categ_id', operator, name)]    
    #    else:              
    #        if name:
    #         domain = ['|', '|', ('name', operator, name), ('default_code', operator, name),
    #                  '|', ('barcode', operator, name), ('categ_id', operator, name)]
    #    return self._search(expression.AND([domain, args]),
    #                              limit=limit, access_rights_uid=name_get_uid)





