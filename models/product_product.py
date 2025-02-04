from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    receta_id = fields.One2many(
        'obrador.recetas',
        string='Receta',
        unique=True
    )