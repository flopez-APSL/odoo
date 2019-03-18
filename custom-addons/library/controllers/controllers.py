# -*- coding: utf-8 -*-
from odoo import http

# class Custom-addons/library(http.Controller):
#     @http.route('/custom-addons/library/custom-addons/library/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom-addons/library/custom-addons/library/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom-addons/library.listing', {
#             'root': '/custom-addons/library/custom-addons/library',
#             'objects': http.request.env['custom-addons/library.custom-addons/library'].search([]),
#         })

#     @http.route('/custom-addons/library/custom-addons/library/objects/<model("custom-addons/library.custom-addons/library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom-addons/library.object', {
#             'object': obj
#         })