# -*- coding: utf-8 -*-
# from odoo import http


# class FieldsSelection(http.Controller):
#     @http.route('/fields_selection/fields_selection/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fields_selection/fields_selection/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fields_selection.listing', {
#             'root': '/fields_selection/fields_selection',
#             'objects': http.request.env['fields_selection.fields_selection'].search([]),
#         })

#     @http.route('/fields_selection/fields_selection/objects/<model("fields_selection.fields_selection"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fields_selection.object', {
#             'object': obj
#         })
