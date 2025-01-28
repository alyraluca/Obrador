from odoo import models, fields, api

class RecetasIngrediente(models.Model):
    _name = 'obrador.receta.ingrediente'
    _description = 'Ingrediente de Receta'

    receta_id = fields.Many2one(
        'obrador.recetas',
        string = 'Receta',
        required=True,
        ondelete = 'cascade'
        )
    producto_id = fields.Many2one(
        'product.product', 
        string='Producto', 
        required=True
    )
    cantidad = fields.Float(string='Cantidad', required=True)
