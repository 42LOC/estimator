from odoo import models, fields, api, _


class HideFields(models.Model):
    _inherit = 'task_estimation.work_units'

    name_seq = fields.Char(string='Work Unit Reference', required=True, copy=False, readonly=True, index=True,
                           default=lambda self: _('New'), invisible='1')
