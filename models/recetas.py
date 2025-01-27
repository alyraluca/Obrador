from odoo import models, fields, api

class Receta(models.Model):
    _name = 'obrador.recetas'
    _description = 'Receta'

    name = fields.Char(string='Nombre')

    alergenos = fields.Selection(
        [('Gluten', 'Gluten'), ('Lactose' , 'Lactosa')],
        string = 'Alergenos'
    )

    tiempo = fields.Integer(string='Tiempo cocción (min)')
    temper = fields.Float(string='Temperatura cocción (ºC)')
    cant = fields.Integer(string='Cantidad producida (u)')
    peso = fields.Float(string='Peso total (g)')

