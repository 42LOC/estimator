# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class estimator(models.Model):
    _name = 'estimator.task_estimation'
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
    units_id = fields.Many2one('task_estimation.work_units', string='Units ID')
    author = fields.Many2one('hr.employee', string="Author")
    total_task_time = fields.Float(store=True, compute="total_task_calc", string="Total Time")

    @api.depends('unit_works_lines.total_time')
    def total_task_calc(self):
        for task in self:
            total = 0.0
            for line in task.unit_works_lines:
                total += line.total_time
            task.total_task_time = total

    @api.model
    def create(self, vals):
        if vals.get('name_task_seq', _('New')) == _('New'):
            vals['name_task_seq'] = self.env['ir.sequence'].next_by_code(
                'estimator.task_estimation.sequence') or _('New')

        result = super(estimator, self).create(vals)
        return result


class TaskEstimationLines(models.Model):
    _name = 'task_estimation.lines'
    _description = 'Task Lines'

    workunit_id = fields.Many2one('task_estimation.work_units', string="Work Unit ID", ondelete="cascade")
    workunit_quantity = fields.Integer(string="Quantity")
    minutes_to_do = fields.Float(string="Time to perform", related="workunit_id.minutes_to_do")
    task_id = fields.Many2one('estimator.task_estimation')
    total_time = fields.Float(store=True, compute="total_calc", string="Total Time (Mins)")

    @api.depends('minutes_to_do', 'workunit_quantity')
    def total_calc(self):
        for record in self:
            record.total_time = record.workunit_id.minutes_to_do * record.workunit_quantity
