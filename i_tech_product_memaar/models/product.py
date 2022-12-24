# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = "product.template"


    yarn_type = fields.Many2one('yarn.type', "Yarn Type")
    total_height = fields.Many2one('total.height', "Total Height")
    loop_weight = fields.Many2one('loop.weight', "Loop Weight")
    gloss_level = fields.Many2one('gloss.level', "Gloss Level")
    base_type = fields.Many2one('base.type', "Base Type")

    yarn_type_setting =fields.Boolean(related="company_id.yarn_type")
    total_height_setting =fields.Boolean(related="company_id.total_height")
    loop_weight_setting =fields.Boolean(related="company_id.loop_weight")
    gloss_level_setting =fields.Boolean(related="company_id.gloss_level")
    base_type_setting =fields.Boolean(related="company_id.base_type")







