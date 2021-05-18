# -*- coding: utf-8 -*-
# from odoo import http


# class UserSelection(http.Controller):
#     @http.route('/user_selection/user_selection/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/user_selection/user_selection/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('user_selection.listing', {
#             'root': '/user_selection/user_selection',
#             'objects': http.request.env['user_selection.user_selection'].search([]),
#         })

#     @http.route('/user_selection/user_selection/objects/<model("user_selection.user_selection"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('user_selection.object', {
#             'object': obj
#         })
