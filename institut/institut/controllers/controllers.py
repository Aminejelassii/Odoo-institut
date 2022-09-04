# -*- coding: utf-8 -*-
# from odoo import http


# class Institut(http.Controller):
#     @http.route('/institut/institut', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/institut/institut/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('institut.listing', {
#             'root': '/institut/institut',
#             'objects': http.request.env['institut.institut'].search([]),
#         })

#     @http.route('/institut/institut/objects/<model("institut.institut"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('institut.object', {
#             'object': obj
#         })
