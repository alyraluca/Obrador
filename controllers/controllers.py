# -*- coding: utf-8 -*-
# from odoo import http


# class Obrador(http.Controller):
#     @http.route('/obrador/obrador/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/obrador/obrador/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('obrador.listing', {
#             'root': '/obrador/obrador',
#             'objects': http.request.env['obrador.obrador'].search([]),
#         })

#     @http.route('/obrador/obrador/objects/<model("obrador.obrador"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('obrador.object', {
#             'object': obj
#         })
