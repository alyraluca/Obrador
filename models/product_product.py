from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    receta_id = fields.One2many(
        'obrador.recetas',
        'producto_id',#Nuevo
        string='Receta',
        unique=True
    )

    
    alergenos_ids = fields.Many2many(
        'obrador.alergenos',
        'product_alergenos_rel',
        'product_id',
        'alergeno_id',
        string='Alérgenos',
        help="Lista de alérgenos presentes en este producto"
    )