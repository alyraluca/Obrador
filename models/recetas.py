from odoo import models, fields, api

class Recetas(models.Model):
    _name = 'obrador.recetas'
    _description = 'Receta'

    name = fields.Char(string='Nombre')

    producto_id = fields.Many2one('product.product', string = 'Producto', required = True)

    tiempo = fields.Integer(string='Tiempo cocción (min)')
    temp = fields.Integer(string='Temp. cocción (ºC)')
    cant = fields.Integer(string='Cantidad prod.(u)')
    peso = fields.Float(string='Peso total (kg)')

    categ = fields.Selection(
        [('Pastries', 'Bolleria'),
         ('Bakery', 'Pasteleria'),
         ('Breads', 'Panes'),
         ('Savoury', 'Salado')],
        string='Categoria',
        required=True
        )

    alergenos_ids = fields.Many2many(
        'obrador.alergenos', #Modelo relacionado
        'recetas_alergenos_rel', #Tabla intermedia
        'receta_id', #Campo en la tabla de ESTE modelo
        'alergeno_id', #Campo en la tabla del modelo relacionado
        string = 'Alérgenos',
        help = 'Selecciona uno o más alérgenos para esta receta'
        
    )

    notas = fields.Text(string = 'Comentarios')

    ingredientes_ids = fields.One2many(
        'obrador.receta.ingrediente',
        'receta_id',
        string='Ingredientes'
    )
    @api.model
    def create(self, values):
        if not values.get('name') and values.get('producto_id'):
            producto = self.env['product.product'].browse(values['producto_id'])
            values['name'] = producto.name
        return super(Recetas, self).create(values)
'''
    @api.onchange('producto_id')
    def _onchange_producto_id(self):
        if self.producto_id and not self.name:
            self.name = self.producto_id.name '''



    



    