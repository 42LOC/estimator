# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class estimator(models.Model):
    _name = 'estimator.task_estimation'
    _description = 'task_estimation.task_estimation'

    name_of_task = fields.Char(string="Task Name", required=True)
    basic_index = fields.Float(string="Basic Index")
    technical_risks = fields.Selection([
        ('1.1', '1.1'),
        ('1.2', '1.2'),
        ('1.4', '1.4'),
    ], string="Technical risks", default='1.1')
    comprehension_index = fields.Selection([
        ('1.2', '1.2'),
        ('1.5', '1.5'),
        ('1.7', '1.7'),
    ], string="Comprehension index", default='1.2')
    hours_perfect = fields.Float(store=True, compute="total_task_calc", string="Perfect (hours)")
    hours_real_time = fields.Float(store=True, compute="calc_peal_time", string="Peal Time (hours)")
    hours_low_performance = fields.Float(store=True, compute="calc_ow_performance", string="Low performance (hours)")
    notes = fields.Text(string="Description")
    unit_works_lines = fields.One2many('task_estimation.lines', 'task_id', string="Tasks Lines")
    name_task_seq = fields.Char(string='Task Estimation Reference', required=True, copy=False, readonly=True,
                                index=True,
                                default=lambda self: _('New'))
    units_id = fields.Many2one('task_estimation.work_units', string='Units ID')
    author = fields.Many2one('hr.employee', string="Author")
    total_task_time = fields.Float(store=True, compute="total_task_calc", string="Total Time (hh:mm)")
    tasks_count = fields.Integer(string='Count of author tasks', compute='get_count_tasks')

    @api.depends('unit_works_lines.total_time')
    def total_task_calc(self):
        for task in self:
            total = 0.0
            for line in task.unit_works_lines:
                total += line.total_time
            task.hours_perfect = total
            task.total_task_time = total

    @api.model
    def create(self, vals):
        if vals.get('name_task_seq', _('New')) == _('New'):
            vals['name_task_seq'] = self.env['ir.sequence'].next_by_code(
                'estimator.task_estimation.sequence') or _('New')

        result = super(estimator, self).create(vals)
        return result

    @api.depends('hours_perfect', 'comprehension_index', 'technical_risks')
    def calc_peal_time(self):
        self.hours_real_time = self.hours_perfect * float(self.technical_risks) * float(self.comprehension_index)

    @api.depends('hours_perfect')
    def calc_ow_performance(self):
        self.hours_low_performance = self.hours_perfect * 1.4 * 1.7

    def tasks_count_author(self):
        return {
            'name': _('Count_tasks'),
            'domain': [('author.id', '=', self.author.id)],
            'res_model': 'estimator.task_estimation',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def get_count_tasks(self):
        count = self.env['estimator.task_estimation'].search_count([('author.id', '=', self.author.id)])
        self.tasks_count = count

class TaskEstimationLines(models.Model):
    _name = 'task_estimation.lines'
    _description = 'Task Lines'

    workunit_id = fields.Many2one('task_estimation.work_units', string="Work Unit ID", ondelete="cascade")
    workunit_quantity = fields.Integer(string="Quantity")
    minutes_to_do = fields.Float(string="Time to perform", related="workunit_id.minutes_to_do")
    task_id = fields.Many2one('estimator.task_estimation')
    total_time = fields.Float(store=True, compute="total_calc", string="Total Time (Hours)")

    @api.depends('minutes_to_do', 'workunit_quantity')
    def total_calc(self):
        for record in self:
            record.total_time = record.workunit_id.minutes_to_do * record.workunit_quantity
