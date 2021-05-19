# -*- coding: utf-8 -*-
# from odoo import http


# class VendaCarros(http.Controller):
#     @http.route('/venda_carros/venda_carros/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/venda_carros/venda_carros/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('venda_carros.listing', {
#             'root': '/venda_carros/venda_carros',
#             'objects': http.request.env['venda_carros.venda_carros'].search([]),
#         })

#     @http.route('/venda_carros/venda_carros/objects/<model("venda_carros.venda_carros"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('venda_carros.object', {
#             'object': obj
#         })
