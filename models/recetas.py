from odoo import models, fields, api
#Modulo para crear recetas

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
        required=True
        )
    
    notas = fields.Text(string = 'Comentarios')
    tiempo = fields.Integer(string='Tiempo cocción (min)') #Tiempo de cocinado
    temp = fields.Integer(string='Temp. cocción (ºC)') #Temperatura de cocción
    cant = fields.Integer(string='Cantidad receta (u)') #Cantidad que produce la receta
    peso = fields.Float(string='Peso total (kg)') #Peso total de los productos elaborados
    receta_instr = fields.Html(string='Instrucciones/Pasos')
    #Campo calculado para la última fecha de producción de ese producto
    ultima_fecha_produc = fields.Datetime(string = 'Última fecha de producción', compute = '_compute_ultima_fecha_produc')
    #Campo calculado para la última cantidad producida
    ultima_cantidad_produc = fields.Float(string= 'Última cantidad producida', compute = '_compute_ultima_cantidad_produc')

    #Categoria para el producto
    categ = fields.Selection(
        [('Pastries', 'Bolleria'),
         ('Bakery', 'Pasteleria'),
         ('Breads', 'Panes'),
         ('Savoury', 'Salado')],
        string='Categoria',
        required=True
        )         

    #Relación Many2many con los alérgenos de los ingredientes: calcula/ recupera los alergenos de la materia prima
    alergenos_ids = fields.Many2many(
        'obrador.alergenos',
        compute='_compute_alergenos',
        store=True
    )

    #Metodo para obtener los alergenos de la materia prima
    @api.depends('ingredientes_ids.producto_id.alergenos_ids')
    def _compute_alergenos(self):
        for receta in self:
            alergenos = set()
            for ingrediente in receta.ingredientes_ids:
                alergenos.update(ingrediente.producto_id.alergenos_ids.ids)  # Obtener los IDs de los alérgenos

            # Guardar los alérgenos en la receta
            receta.alergenos_ids = [(6, 0, list(alergenos))]

            # Guardar los alérgenos también en el producto asociado
            if receta.producto_id:
                receta.producto_id.alergenos_ids = [(6, 0, list(alergenos))]


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

    #Metodo para recuperar la última cantidad producida
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
    
    #Constraints para que solo haya una receta por producto
    _sql_constraints = [
        ('unique_receta_producto', 'UNIQUE(producto_id)', 'Cada producto solo puede tener una receta asociada')
    ]


    