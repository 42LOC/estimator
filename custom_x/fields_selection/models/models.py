from odoo import models, fields, api


class FieldsSelection(models.Model):
    _inherit = 'task_estimation.task_estimation'

    comprehension_index = fields.Selection([
        ('1.2', '1.2'),
        ('1.5', '1.5'),
        ('1.7', '1.7')],
        string="Comprehension Index")
    technical_risks = fields.Selection([
        ('1.1', '1.1'),
        ('1.2', '1.2'),
        ('1.4', '1.4')],
        string="Technical Risks")
