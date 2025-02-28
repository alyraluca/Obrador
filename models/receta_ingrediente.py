from odoo import models, fields, api
#Modulo para añadir dentro del formulario de 'Recetas'

class RecetasIngrediente(models.Model):
    _name = 'obrador.receta.ingrediente'
    _description = 'Ingrediente de Receta'

    #Relación Many2one con las recetas
    receta_id = fields.Many2one(
        'obrador.recetas',
        string = 'Receta',
        required=True,
        ondelete = 'cascade'
        )
    #Relación Many2one con los productos del modulo de produst.product 
    producto_id = fields.Many2one(
        'product.product', 
        string='Producto', 
        required=True
    )
    cantidad = fields.Float(string='Cantidad', required=True)

    unidad_medida_id = fields.Char(string='Unidad', required=True)

    alergenos_ids = fields.Many2many(
        'obrador.alergenos',
        compute='_compute_alergenos',
        store=True,
        ondelete = 'cascade',
        compute_sudo=True #New
    )

    #Metodo para guardar la relación con los alergenos y que aparezca en la ficha del producto
    def write(self, values):
        res = super(RecetasIngrediente, self).write(values)
        if 'producto_id' in values or 'alergenos_ids' in values:
            if self.receta_id:
                self.receta_id._compute_alergenos()  # Volver a calcular los alérgenos de la receta
        return res


    #
    @api.depends('producto_id.alergenos_ids')
    def _compute_alergenos(self):
        for ingrediente in self:
            ingrediente.alergenos_ids = [(6, 0, ingrediente.producto_id.alergenos_ids.ids)]

    '''@api.depends('producto_id.alergenos_ids')
    def _compute_alergenos(self):
        for ingrediente in self:
            ingrediente.alergenos_ids = ingrediente.producto_id.alergenos_ids'''
    
    