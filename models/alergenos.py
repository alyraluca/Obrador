from odoo import models, fields, api

class Alergenos(models.Model):
    _name = 'obrador.alergenos'
    _description = 'Alergenos'

    name = fields.Char(string='Nombre')