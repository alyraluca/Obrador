import logging
from odoo import models, fields, api
from datetime import date

_logger = logging.getLogger(__name__)

class TPVCierreAutomatico(models.Model):
    _inherit = "pos.session"

    @api.model
    def auto_close_pos_sesion(self):
        '''Cierra automáticamente todas las sesiones TPV 
        abiertas a las 23:95 y luego registra las sobras en el módulo de Obrador'''
        sesiones_abiertas = self.search([("state", "=", "opened")])

        for sesion in sesiones_abiertas:
            try:
                sesion.action_pos_session_closing_control()
                _logger.info(f"Sessión {sesion.name} cerrada automáticamente")
            
            except Exception as e:
                _logger.error(f"Error cerrando sesión {sesion.name}: {str(e)}")
            
            #Despues de cerrar todas las sesiones, calcular las sobras del día
            #self.env["obrador.remanentes"].calcular_sobras_diarias()
            _logger.info("Cálculo de sobras ejecutado despúes del cierre automático del TPV")
            

