# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class task_estimation(models.Model):
    _name = 'task_estimation.task_estimation'
    _description = 'task_estimation.task_estimation'

    name_of_task = fields.Char(string="Task Name", required=True)
    basic_index = fields.Float(string="Basic Index")
    comprehension_index = fields.Float(string="Comprehension Index")
    technical_risks = fields.Float(string="Technical Risks")

    hours_perfect = fields.Float(string="Perfect (hours)")
    hours_real_time = fields.Float(string="Peal Time (hours)")
    hours_low_performance = fields.Float(string="Low performance (hours)")
    notes = fields.Text(string="Description")
    unit_works_lines = fields.One2many('task_estimation.lines', 'task_id', string="Tasks Lines")
    name_task_seq = fields.Char(string='Task Estimation Reference', required=True, copy=False, readonly=True,
                                index=True,
                                default=lambda self: _('New'))

    total_time = fields.Float(compute="_value_pc", store=True)


    @api.depends('unit_works_lines')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.) / 100


    @api.model
    def create(self, vals):
        if vals.get('name_task_seq', _('New')) == _('New'):
            vals['name_task_seq'] = self.env['ir.sequence'].next_by_code('task_estimation.task_estimation.sequence') or _('New')

        result = super(task_estimation, self).create(vals)
        return result


class TaskEstimationLines(models.Model):
    _name = 'task_estimation.lines'
    _description = 'Task Lines'

    workunit_id = fields.Many2one('task_estimation.work_units', string="Work Unit ID", ondelete="cascade")
    workunit_quantity = fields.Integer(string="Quantity")
    task_id = fields.Many2one('task_estimation.task_estimation', invisible=True)
