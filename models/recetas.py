from odoo import models, fields, api

class Recetas(models.Model):
    _name = 'obrador.recetas'
    _description = 'Receta'

    name = fields.Char(string='Nombre')
    
    #Relación Many2one con los productos. UNA receta solo puede estar relacionada con UN producto
    #Reemplaza el One2one
    producto_id = fields.Many2one(
        'product.product', 
        string = 'Producto', 
        ondelete="cascade", 
        unique=True, 
        required=True
        )
    
    notas = fields.Text(string = 'Comentarios')
    tiempo = fields.Integer(string='Tiempo cocción (min)')
    temp = fields.Integer(string='Temp. cocción (ºC)')
    cant = fields.Integer(string='Cantidad receta (u)')
    peso = fields.Float(string='Peso total (kg)')
    receta_instr = fields.Html(string='Instrucciones/Pasos')
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
        help = 'Alérgenos detectados en los ingredientes de la receta'#Nuevo
        
    )
    

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
    
    _sql_constraints = [
        ('unique_receta_producto', 'UNIQUE(producto_id)', 'Cada producto solo puede tener una receta asociada')
    ]

    #Nuevo
    @api.model
    def create(self, vals):
        receta = super(Recetas, self).create(vals)
        receta._actualizar_alergenos()
        return receta

    def write(self, vals):
        res = super(Recetas, self).write(vals)
        self._actualizar_alergenos()
        return res
    
    def _actualizar_alergenos(self):
        for receta in self:
            alergenos = receta.ingredientes_ids.mapped('producto_id.alergenos_ids')
            receta.alergenos_ids = [(6,0,alergenos.ids)]
    


     '''
    #Nuevo
    @api.onchange('ingredientes_ids')
    def _update_alergenos_from_ingredientes(self):
        for receta in self:
            alergenos = receta.ingredientes_ids.mapped('producto_id_alergenos_ids')
            receta.alergenos_ids = [(6,0, alergenos.ids)]
    '''
    