from odoo import models, fields, api

class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    alergenos_ids = fields.Many2many(
        'obrador.alergenos',
        'product_alergenos_rel',
        'product_id',
        'alergeno_id',
        string='Alérgenos',
        help='Lista de alérgenos presentes en este producto',
        
    )
    perecedero = fields.Boolean(
        string="Perecedero", 
        default = False
        )
    
    receta_id = fields.Many2one(
        'obrador.recetas', 
        string="Receta", 
        compute='_compute_receta', 
        #store=True, 
        help="Receta asociada a este producto"
    )

    @api.depends('product_variant_ids')
    def _compute_receta(self):
        for record in self:
            producto = record.product_variant_ids[:1] 
            if producto:
                receta = self.env['obrador.recetas'].search([('producto_id', '=', producto.id)], limit=1)
                record.receta_id = receta.id if receta else False