from odoo import models, fields, api

class ProductProduct(models.Model):
    _name = 'product.product'
    _inherit = 'product.product'

    receta_id = fields.One2many(
        'obrador.recetas',
        'producto_id',
        string='Receta'
    )

    
    