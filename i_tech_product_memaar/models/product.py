# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    yarn_type = fields.Many2one('yarn.type', "Yarn Type")
    total_height = fields.Many2one('total.height', "Total Height")
    loop_weight = fields.Many2one('loop.weight', "Loop Weight")



    #@api.model
    def _aomunt(self):
        company_id = self.env.company.id
        print(company_id)
        #return {'domain': {'journal_id': [('journal_user_id', '=', self.env.user.name)]}}    





