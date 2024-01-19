# -*- coding: utf-8 -*-
# from odoo import http


# class ProduccionMod2(http.Controller):
#     @http.route('/produccion_mod2/produccion_mod2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/produccion_mod2/produccion_mod2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('produccion_mod2.listing', {
#             'root': '/produccion_mod2/produccion_mod2',
#             'objects': http.request.env['produccion_mod2.produccion_mod2'].search([]),
#         })

#     @http.route('/produccion_mod2/produccion_mod2/objects/<model("produccion_mod2.produccion_mod2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('produccion_mod2.object', {
#             'object': obj
#         })
