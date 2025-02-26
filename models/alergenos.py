from odoo import models, fields, api

class Alergenos(models.Model):
    _name = 'obrador.alergenos'
    _description = 'Alergenos'

    name = fields.Char(string='Nombre')
    product_count  = fields.Integer(string='Número de productos', compute = '_compute_product_count', store = True)
    product_tags = fields.Char(string = "Productos con este alérgeno", compute = '_compute_product_tags', store = True)

    #Relación Many2many con las recetas
    recetas_ids = fields.Many2many(
        'obrador.recetas',
        'receta_alergenos_rel',
        'alergeno_id',
        'receta_id',
        string='Recetas'
    )
    #Many2many con product.template
    product_ids = fields.Many2many(
        'product.template',
        'product_alergenos_rel',
        'alergeno_id',
        'product_id',
        string='Productos'
    )

    @api.depends('product_ids')
    def _compute_product_count(self):
        for record in self:
            record.product_count = len(record.product_ids)

    @api.depends('product_ids')
    def _compute_product_tags(self):
        for record in self:
            productos_names = record.product_ids.mapped('name')
            record.product_tags = ', '.join(productos_names) if productos_names else ''


    '''@api.depends('product_ids.receta_id')
    def _compute_recetas_ids(self):
        """Calcula las recetas que contienen este alérgeno a través de los productos y sus ingredientes"""
        for alergeno in self:
            recetas = self.env['obrador.recetas'].search([
                ('ingredientes_ids.producto_id.alergenos_ids', 'in', alergeno.id)
            ])
            alergeno.recetas_ids = [(6, 0, recetas.ids)]  # Establece los IDs de las recetas encontradas

    @api.depends('recetas_ids')
    def _compute_recetas_count(self):
        """Cuenta todas las recetas que tienen este alérgeno"""
        for record in self:
            record.recetas_count = len(record.recetas_ids)

    @api.depends('recetas_ids')
    def _compute_recetas_tags(self):
        """Genera una lista de nombres de recetas que contienen este alérgeno"""
        for record in self:
            recetas_names = record.recetas_ids.mapped('name')
            record.recetas_tags = ', '.join(recetas_names) if recetas_names else '''''

