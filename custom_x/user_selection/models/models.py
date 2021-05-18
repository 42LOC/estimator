from odoo import models, fields, api


class UserSelection(models.Model):
    _inherit = 'task_estimation.task_estimation'

    author = fields.Many2one('res.partner', string='Author')
