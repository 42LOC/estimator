# -*- coding: utf-8 -*-
# from odoo import http


# class HideLineCalc(http.Controller):
#     @http.route('/hide_line_calc/hide_line_calc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hide_line_calc/hide_line_calc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hide_line_calc.listing', {
#             'root': '/hide_line_calc/hide_line_calc',
#             'objects': http.request.env['hide_line_calc.hide_line_calc'].search([]),
#         })

#     @http.route('/hide_line_calc/hide_line_calc/objects/<model("hide_line_calc.hide_line_calc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hide_line_calc.object', {
#             'object': obj
#         })
