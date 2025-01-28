from odoo import models, fields, api

class Alergenos(models.Model):
    _name = 'obrador.alergenos'
    _description = 'Alergenos'

    name = fields.Char(string='Nombre')

    recetas_count  = fields.Integer(string='Número de recetas', compute = '_compute_recetas_count')

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