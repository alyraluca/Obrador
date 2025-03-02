from odoo import models, fields, api
'''Metodo heredado de product_template para gestionar la relación entre los 
alergenos, las recetas y los productos'''

class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    #Relación Many2many con los alergenos
    alergenos_ids = fields.Many2many(
        'obrador.alergenos',
        'product_alergenos_rel',
        'product_id',
        'alergeno_id',
        string='Alérgenos',
        help='Lista de alérgenos presentes en este producto',
        store=True
    )

    #Campo para determinar si el producto es elaborado o solo es materia prima
    perecedero = fields.Boolean(
        string="Elaborado", 
        default = False
        )
    
    #Campo calculado para recuperar la receta asociado al producto
    receta_id = fields.Many2one(
        'obrador.recetas', 
        string="Receta", 
        compute='_compute_receta', 
        help="Receta asociada a este producto"
    )

    #Metodo para obtener la receta del producto
    @api.depends('product_variant_ids')
    def _compute_receta(self):
        for record in self:
            producto = record.product_variant_ids[:1] 
            if producto:
                receta = self.env['obrador.recetas'].search([('producto_id', '=', producto.id)], limit=1)
                record.receta_id = receta.id if receta else False
    
    