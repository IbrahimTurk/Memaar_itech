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

class Shade_Type(models.Model):
    _name = 'gloss.level'
    _rec_name = 'name'

    name = fields.Char()
    sequence_code = fields.Char('Sequence',required=True)

class Shade_Type(models.Model):
    _name = 'base.type'
    _rec_name = 'name'

    name = fields.Char()
    sequence_code = fields.Char('Sequence',required=True)        
