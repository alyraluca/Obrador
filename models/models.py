# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class produccion_mod2(models.Model):
#     _name = 'produccion_mod2.produccion_mod2'
#     _description = 'produccion_mod2.produccion_mod2'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
