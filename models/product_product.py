from odoo import models, fields, api

class ProductProduct(models.Model):
    _name = 'product.product'
    _inherit = 'product.product'

    #Relación que imita el One2one con recetas, ya que solo se puede crear una receta por producto
    receta_id = fields.One2many(
        'obrador.recetas',
        'producto_id',
        string='Receta'
    )

    
    