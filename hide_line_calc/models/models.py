from odoo import models, fields, api


class HideLineCalc(models.Model):
    _inherit = 'task_estimation.task_estimation'

    unit_works_lines = fields.One2many('task_estimation.lines', 'task_id', string="Tasks Lines")
    total_task_time = fields.Float(compute="total_task_calc", string="Perfect (Hours)")
    hours_real_time = fields.Float(compute='peal_time_calc', string="Peal Time (hours)")
    hours_low_performance = fields.Float(compute='low_performance_calc', string="Low performance (hours)")

    @api.depends('total_task_time')
    def low_performance_calc(self):
        self.hours_low_performance = self.total_task_time * 1.4 * 1.7

    @api.depends('total_task_time', 'comprehension_index', 'technical_risks')
    def peal_time_calc(self):
        self.hours_real_time = self.total_task_time * float(self.comprehension_index) * float(self.technical_risks)
