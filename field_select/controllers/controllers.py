# -*- coding: utf-8 -*-
# from odoo import http


# class FieldSelect(http.Controller):
#     @http.route('/field_select/field_select/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/field_select/field_select/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('field_select.listing', {
#             'root': '/field_select/field_select',
#             'objects': http.request.env['field_select.field_select'].search([]),
#         })

#     @http.route('/field_select/field_select/objects/<model("field_select.field_select"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('field_select.object', {
#             'object': obj
#         })
