# -*- coding: utf-8 -*-
# from odoo import http


# class UserField(http.Controller):
#     @http.route('/user_field/user_field/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/user_field/user_field/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('user_field.listing', {
#             'root': '/user_field/user_field',
#             'objects': http.request.env['user_field.user_field'].search([]),
#         })

#     @http.route('/user_field/user_field/objects/<model("user_field.user_field"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('user_field.object', {
#             'object': obj
#         })
