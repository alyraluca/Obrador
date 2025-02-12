from odoo import models, fields, api

class Alergenos(models.Model):
    _name = 'obrador.alergenos'
    _description = 'Alergenos'

    name = fields.Char(string='Nombre')
    recetas_count  = fields.Integer(string='Número de recetas', compute = '_compute_recetas_count')
    recetas_tags = fields.Char(string = "Recetas con este alérgeno", compute = '_compute_recetas_tags')

    #Contar todas las recetas que tienen ese alergeno
    @api.depends('recetas_ids')
    def _compute_recetas_count(self):
        for record in self:
            record.recetas_count = len(record.recetas_ids)

    
    #Relación Many2many con las recetas
    recetas_ids = fields.Many2many(
        'obrador.recetas', 
        'recetas_alergenos_rel',
        'alergeno_id',
        'receta_id',
        string = 'Recetas'
    )
    #Many2many con product.template
    product_ids = fields.Many2many(
        'product.template',
        'product_alergenos_rel',
        'alergeno_id',
        'product_id',
        string='Productos'
    )

    #Obtener los nombres de las recetas para visualizarlas en la lista
    @api.depends('recetas_ids')
    def _compute_recetas_tags(self):
        for record in self:
            recetas_names = [receta.name for receta in record.recetas_ids]
            record.recetas_tags = ', '.join(recetas_names) if recetas_names else ''

