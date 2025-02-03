from odoo import models, fields, api

class ProductInherit(models.Model):
    _inherit = 'product.product'

    #Campo Many2many para enlazarlo con los alérgeno
    alergenos_ids = fields.Many2many(
        'obrador.alergenos',
        'product_alergenos_rel',
        'product_id',
        'alergeno_id',
        string = 'Alérgeno'
    )

    #Relación Many2one con la receta (simulando one2one)
    receta_id = fields.Many2one(
        'obrador.recetas',
        string = "Receta"
    )

    