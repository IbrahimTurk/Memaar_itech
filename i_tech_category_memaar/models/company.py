# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CompanyFields(models.Model):
    _inherit = "res.company"

    category_search = fields.Boolean("Category Search")




