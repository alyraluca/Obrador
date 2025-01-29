from odoo import models, fields, api

class Recetas(models.Model):
    _name = 'obrador.recetas'
    _description = 'Receta'

    name = fields.Char(string='Nombre')

    #Relación Many2one con los productos. UNA receta solo puede estar relacionada con UN producto
    #Mientras un producto puede estar relacionado con muchas recetas
    producto_id = fields.Many2one('product.product', string = 'Producto', required = True)

    tiempo = fields.Integer(string='Tiempo cocción (min)')
    temp = fields.Integer(string='Temp. cocción (ºC)')
    cant = fields.Integer(string='Cantidad receta (u)')
    peso = fields.Float(string='Peso total (kg)')
    #Campo calculado para la fecha de producción
    ultima_fecha_produc = fields.Datetime(string = 'Última fecha de producción', compute = '_compute_ultima_fecha_produc')
    ultima_cantidad_produc = fields.Float(string= 'Última cantidad producida', compute = '_compute_ultima_cantidad_produc')

    categ = fields.Selection(
        [('Pastries', 'Bolleria'),
         ('Bakery', 'Pasteleria'),
         ('Breads', 'Panes'),
         ('Savoury', 'Salado')],
        string='Categoria',
        required=True
        )

    #Relación Many2many con los alérgenos
    alergenos_ids = fields.Many2many(
        'obrador.alergenos', #Modelo relacionado
        'recetas_alergenos_rel', #Tabla intermedia
        'receta_id', #Campo en la tabla de ESTE modelo
        'alergeno_id', #Campo en la tabla del modelo relacionado
        string = 'Alérgenos',
        help = 'Selecciona uno o más alérgenos para esta receta'
        
    )

    notas = fields.Text(string = 'Comentarios')

    #Relación One2many con los ingredientes del modulo receta_ingrediente 
    ingredientes_ids = fields.One2many(
        'obrador.receta.ingrediente',
        'receta_id',
        string='Ingredientes'
    )
    #Sobreescribir el metodo de crear para ponerle el mismo nombre a la receta que el del producto
    @api.model
    def create(self, values):
        if not values.get('name') and values.get('producto_id'):
            producto = self.env['product.product'].browse(values['producto_id'])
            values['name'] = producto.name
        return super(Recetas, self).create(values)

    #Campo calculado para almacenar la última fecha de producción del producto asociado a la receta
    @api.depends('producto_id')
    def _compute_ultima_fecha_produc(self):
        for record in self:
            ultima_produc = self.env['mrp.production'].search( # Realizamos la busqueda en el modelo
                [
                    ('product_id', '=', record.producto_id.id),
                    ('state', '=', 'done') #Solo tenemos en cuenta las ordenes acabadas
                ], order = 'date_finished desc', limit=1 #Ordenamos de forma descendente y lo limitamos a una orden
            )
            if ultima_produc:
                record.ultima_fecha_produc = ultima_produc.date_finished
            else:
                record.ultima_fecha_produc = False

    @api.depends('producto_id')
    def _ultima_cantidad_produc(self):
        for record in self:
            ultima_produc = self.env['mrp.production'].search( # Realizamos la busqueda en el modelo
                [
                    ('product_id', '=', record.producto_id.id),
                    ('state', '=', 'done') #Solo tenemos en cuenta las ordenes acabadas
                ], order = 'date_finished desc', limit=1 #Ordenamos de forma descendente y lo limitamos a una orden
            )
            if ultima_produc:
                record.ultima_cantidad_produc = ultima_produc.qty_producing
            else:
                record.ultima_cantidad_produc = 0.0

    
'''> /usr/lib/python3/dist-packages/odoo/fields.py(80)determine()
odoodock-web-1     | -> needle = getattr(records, needle)
'''


    