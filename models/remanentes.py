from odoo import models, fields, api
from datetime import date, datetime, time



class Remanentes(models.Model):
    _name ='obrador.remanentes'
    _description = 'Remanentes' 
    
    _order = "fecha desc"
    
    producto_id = fields.Many2one(
        'product.template',
        string = "Producto",
        domain = [('perecedero', '=', True)],
        required = True
    )

    fecha = fields.Date(string="Fecha", default = fields.Date.context_today, required=True)
    sobras = fields.Float(string="Sobrante", required = True)
    produccion = fields.Float(string="Cantidad producida", 
                                compute = "_compute_cantidad_producida",
                                store = True)

    @api.depends('producto_id', 'fecha')
    def _compute_cantidad_producida(self):
        """Calcula la cantidad producida del producto en la fecha ingresada."""
        for record in self:
            if record.producto_id and record.fecha:
                fecha_inicio = fields.Datetime.to_datetime(record.fecha)  # 00:00:00 del día seleccionado
                fecha_fin = datetime.combine(record.fecha, time(23,59,59))
                # Busca registros de producción en la fecha dada
                produccion = self.env['mrp.production'].search([
                    ('product_id', '=', record.producto_id.id),
                    ('date_planned_start', '>=', fecha_inicio),
                    ('date_planned_start', '<', fecha_fin)
                ])
                
                # Suma la cantidad producida en esa fecha
                record.produccion = sum(produccion.mapped('product_qty'))
            else:
                record.produccion = 0.0
    
    _sql_constraints = [
    ('unique_product_per_day', 'UNIQUE(producto_id, fecha)',
        'Ya existe un registro de sobras para este producto en la fecha seleccionada.')]




    