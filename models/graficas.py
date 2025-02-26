from odoo import models, fields, api

class Graficas(models.Model):
    _name = 'obrador.graficas'
    _description = 'Gráficas'
    _auto = False

    fecha = fields.Date(string="Fecha")
    produccion = fields.Float(string="Cantidad producida")
    sobras = fields.Float(string="Sobrantes")
    nombre = fields.Char(string="Producto")

    @api.model
    def init(self):
        self.env.cr.execute("""
            DROP VIEW IF EXISTS obrador_graficas;
            CREATE OR REPLACE VIEW obrador_graficas AS (
                SELECT
                    r.id, 
                    r.fecha, 
                    r.sobras,
                    r.produccion,
                    p.name AS nombre
                FROM obrador_remanentes r
                LEFT JOIN product_template p ON p.id = r.producto_id
            );
        """
        )