# -*- coding: utf-8 -*-
# from odoo import http


# class ModPrueba(http.Controller):
#     @http.route('/mod_prueba/mod_prueba', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mod_prueba/mod_prueba/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mod_prueba.listing', {
#             'root': '/mod_prueba/mod_prueba',
#             'objects': http.request.env['mod_prueba.mod_prueba'].search([]),
#         })

#     @http.route('/mod_prueba/mod_prueba/objects/<model("mod_prueba.mod_prueba"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mod_prueba.object', {
#             'object': obj
#         })

