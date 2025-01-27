from odoo import models, fields, api

class Recetas(models.Model):
    _name = 'obrador.recetas'
    _description = 'Receta'

    name = fields.Char(string='Nombre', required=True, help = 'Nombre de la receta')

    tiempo = fields.Integer(string='Tiempo cocción (min)')
    temper = fields.Integer(string='Temp. cocción (ºC)')
    cant = fields.Integer(string='Cantidad prod.(u)')
    peso = fields.Float(string='Peso total (kg)')

    categ = fields.Selection(
        [('Pastries', 'Bolleria'),
         ('Bakery', 'Pasteleria'),
         ('Breads', 'Panes'),
         ('Savoury', 'Salado')],
        string='Categoria')

    alergenos = fields.Selection(
        [('Gluten', 'Gluten'), ('Lactose' , 'Lactosa')],
        string = 'Alergenos',
        required=True
    )

    notas = fields.Text(string = 'Comentarios')

    