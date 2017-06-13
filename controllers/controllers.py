# -*- coding: utf-8 -*-
from odoo import http

# class LocalAddons/loans(http.Controller):
#     @http.route('/local_addons/loans/local_addons/loans/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/local_addons/loans/local_addons/loans/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('local_addons/loans.listing', {
#             'root': '/local_addons/loans/local_addons/loans',
#             'objects': http.request.env['local_addons/loans.local_addons/loans'].search([]),
#         })

#     @http.route('/local_addons/loans/local_addons/loans/objects/<model("local_addons/loans.local_addons/loans"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('local_addons/loans.object', {
#             'object': obj
#         })