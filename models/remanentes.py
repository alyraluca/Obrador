from odoo import models, fields, api
from datetime import date, datetime, time
#Modulo para gestionar las sobras de los productos


class Remanentes(models.Model):
    _name ='obrador.remanentes'
    _description = 'Remanentes' 
    
    #Ordenamos las sobras de manera descendente
    _order = "fecha desc"
    
    '''
    Relación Many2one con product.template que solo nos enseña los productos 
    'elaborados' para los cuales podemos crear sobras
    '''
    producto_id = fields.Many2one(
        'product.template',
        string = "Producto",
        domain = [('perecedero', '=', True)],
        required = True
    )

    #Field para la fecha, que por defecto escoje la fecha del día 
    fecha = fields.Date(string="Fecha", default = fields.Date.context_today, required=True)
    sobras = fields.Float(string="Sobrante", required = True)
    #Field que calcula la cantidad producida de la fecha escogida para la sobra
    produccion = fields.Float(string="Cantidad producida", 
                                compute = "_compute_cantidad_producida",
                                store = True)

    #Metodo para calular la cantidad elaborada el día de la producción
    @api.depends('producto_id', 'fecha')
    def _compute_cantidad_producida(self):
        for record in self:
            if record.producto_id and record.fecha:
                fecha_inicio = fields.Datetime.to_datetime(record.fecha)
                fecha_fin = datetime.combine(record.fecha, time(23,59,59))
                # Busca registros de producción en la fecha dada
                produccion = self.env['mrp.production'].search([
                    ('product_id', '=', record.producto_id.id),
                    ('date_planned_start', '>=', fecha_inicio),
                    ('date_planned_start', '<', fecha_fin)
                ])
                
                # Suma la cantidad producida en esa fecha (si hay varias elaboraciones, las suma todas)
                record.produccion = sum(produccion.mapped('product_qty'))
            else:
                record.produccion = 0.0
    
    #Contraint para permitir solo un registro por producto por día
    _sql_constraints = [
    ('unique_product_per_day', 'UNIQUE(producto_id, fecha)',
        'Ya existe un registro de sobras para este producto en la fecha seleccionada.')]




    