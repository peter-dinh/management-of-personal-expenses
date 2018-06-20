# -*- coding: utf-8 -*-
from odoo import http

# class AppDemo(http.Controller):
#     @http.route('/app_demo/app_demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/app_demo/app_demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('app_demo.listing', {
#             'root': '/app_demo/app_demo',
#             'objects': http.request.env['app_demo.app_demo'].search([]),
#         })

#     @http.route('/app_demo/app_demo/objects/<model("app_demo.app_demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('app_demo.object', {
#             'object': obj
#         })