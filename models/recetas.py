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
        string='Categoria',
        required=True)

    alergenos_ids = fields.Many2many(
        'obrador.alergenos',
        string = 'Alérgenos',
        help = 'Selecciona uno o más alérgenos para esta receta'
        #required=True
    )

    notas = fields.Text(string = 'Comentarios')

    