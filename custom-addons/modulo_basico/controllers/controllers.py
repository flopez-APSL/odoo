# -*- coding: utf-8 -*-
from odoo import http

# class ModuloBase(http.Controller):
#     @http.route('/modulo_basico/modulo_basico/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_basico/modulo_basico/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_basico.listing', {
#             'root': '/modulo_basico/modulo_basico',
#             'objects': http.request.env['modulo_basico.modulo_basico'].search([]),
#         })

#     @http.route('/modulo_basico/modulo_basico/objects/<model("modulo_basico.modulo_basico"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_basico.object', {
#             'object': obj
#         })