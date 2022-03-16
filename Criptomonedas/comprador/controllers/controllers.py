# -*- coding: utf-8 -*-
# from odoo import http


# class Comprador(http.Controller):
#     @http.route('/comprador/comprador/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/comprador/comprador/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('comprador.listing', {
#             'root': '/comprador/comprador',
#             'objects': http.request.env['comprador.comprador'].search([]),
#         })

#     @http.route('/comprador/comprador/objects/<model("comprador.comprador"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('comprador.object', {
#             'object': obj
#         })
