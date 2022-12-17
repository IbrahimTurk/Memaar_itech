from odoo import api, fields, models


class YarnType(models.Model):
    _name = 'yarn.type'
    _rec_name = 'name'

    name = fields.Char()



class TotalHeight(models.Model):
    _name = 'total.height'
    _rec_name = 'name'

    name = fields.Char()    


class LoopWeight(models.Model):
    _name = 'loop.weight'
    _rec_name = 'name'

    name = fields.Char()    
