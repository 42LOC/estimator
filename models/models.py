# -*- coding: utf-8 -*-

from odoo import models, fields, api


class task_estimation(models.Model):
    _name = 'task_estimation.task_estimation'
    _description = 'task_estimation.task_estimation'

    name_of_task = fields.Char(string="Task Name")
    basic_index = fields.Float(string="Basic Index")
    comprehension_index = fields.Float(string="Comprehension Index")
    technical_risks = fields.Float(string="Technical Risks")

    hours_perfect = fields.Float(string="Perfect (hours)")
    hours_real_time = fields.Float(string="Peal Time (hours)")
    hours_low_performance = fields.Float(string="Low performance (hours)")



    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
