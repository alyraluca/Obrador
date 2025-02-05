from odoo import models, fields, api
#Modulo para añadir dentro del formulario de 'Recetas'

class RecetasIngrediente(models.Model):
    _name = 'obrador.receta.ingrediente'
    _description = 'Ingrediente de Receta'

    #Relación Many2one con las recetas
    receta_id = fields.Many2one(
        'obrador.recetas',
        string = 'Receta',
        required=True,
        ondelete = 'cascade'
        )
    #Relación Many2one con los productos del modulo de produst.product 
    producto_id = fields.Many2one(
        'product.product', 
        string='Producto', 
        required=True
    )
    cantidad = fields.Float(string='Cantidad', required=True)

    unidad_medida_id = fields.Char(string='Unidad', required=True)
