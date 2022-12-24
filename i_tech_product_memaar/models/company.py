# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CompanyFields(models.Model):
    _inherit = "res.company"

    yarn_type = fields.Boolean("Yarn Type")
    total_height = fields.Boolean("Total Height")
    loop_weight = fields.Boolean("Loop Weight")
    gloss_level = fields.Boolean("Gloss Level")
    base_type = fields.Boolean("Base Type")



