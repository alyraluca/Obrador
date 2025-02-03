from odoo import models, fields, api

class Recetas(models.Model):
    _name = 'obrador.recetas'
    _description = 'Receta'

    name = fields.Char(string='Nombre')

    #Relación de varios productos/materia prima a una receta
    producto_ids = fields.One2many(
        'product.product',
        'receta_id',
        string= 'Producto'
    )
    #Facilita la relación con un solo producto 
    producto_id = fields.Many2one(
        'product.product',
        compute = '_compute_producto_id',
        inverse = '_inverse_producto_id',
        store=True,
        string = 'Producto', 
        
        )

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
        compute = '_compute_alergenos',
        store=True,
        string = 'Alérgenos',

        
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
    def _compute_ultima_cantidad_produc(self):
        for record in self:
            ultima_produc = self.env['mrp.production'].search( # Realizamos la busqueda en el modelo
                [
                    ('product_id', '=', record.producto_id.id),
                    ('state', '=', 'done') #Solo tenemos en cuenta las ordenes acabadas
                ], order = 'date_finished desc', limit=1 #Ordenamos de forma descendente y lo limitamos a una orden
            )
            if ultima_produc:
                record.ultima_cantidad_produc = ultima_produc.product_qty
            else:
                record.ultima_cantidad_produc = 0.0
    
    #Se ejecuta automaticamente cuando cammbia el producto (para mantener el one2one con productos)
    @api.depends('producto_ids')
    def _compute_producto_id(self):
        for record in self:
            record.producto_id = record.producto_ids[:1].id if record.producto_ids else False
    
    def _inverse_producto_id(self):
        for record in self:
            if record.producto_ids:
                record.producto_ids.receta_id = False
            if record.producto_id:
                record.producto_id.receta_id = record
    
    #Enseñar automaticamente los alergenos una vez añadido los ingredientes
    @api.depends('producto_id.alergenos_ids')
    def _compute_alergenos(self):
        for record in self:
            record.alergenos_ids = record.producto_id.alergenos_ids 
    



    