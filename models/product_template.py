from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    alergenos_ids = fields.Many2many(
        'obrador.alergenos',
        'product_alergenos_rel',
        'product_id',
        'alergeno_id',
        string='Alérgenos',
        help='Lista de alérgenos presentes en este producto'
    )