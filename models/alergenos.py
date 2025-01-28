from odoo import models, fields, api

class Alergenos(models.Model):
    _name = 'obrador.alergenos'
    _description = 'Alergenos'

    name = fields.Char(string='Nombre')
    recetas_count  = fields.Integer(string='Número de recetas', compute = '_compute_recetas_count')
    #recetas_tags = fields.Char(string = "Recetas con este alérgeno", compute = '_compute_recetas_tags')

    
    #Relación Many2many con las recetas
    recetas_ids = fields.Many2many(
        'obrador.recetas', 
        'recetas_alergenos_rel',
        'alergeno_id',
        'receta_id',
        string = 'Recetas'
    )
    #Contar todas las recetas que tienen ese alergeno
    @api.depends('recetas_ids')
    def _compute_recetas_count(self):
        for record in self:
            record.recetas_count = len(record.recetas_ids)

    #Obtener los nombres de las recetas
    """ @api.depends('recetas_ids')
    def _compute_recetas_tags(self):
        for record in self:
            recetas_names = [receta.name for receta in record.recetas_ids]
            record.recetas_tags = ', '.join(recetas_names) if recetas_names else '' """
            