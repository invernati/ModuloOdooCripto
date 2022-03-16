# -*- coding: utf-8 -*-
# from odoo import http


# class Reparto(http.Controller):
#     @http.route('/reparto/reparto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reparto/reparto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('reparto.listing', {
#             'root': '/reparto/reparto',
#             'objects': http.request.env['reparto.reparto'].search([]),
#         })

#     @http.route('/reparto/reparto/objects/<model("reparto.reparto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reparto.object', {
#             'object': obj
#         })
