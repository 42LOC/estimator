
from odoo import models, fields, api

class WorkUnits(models.Model):
    _name = "task_estimation.work_units"
    _description = 'task_estimation.work_units'

    name_unit = fields.Char(string="Name of Unit")
    minutes_to_do = fields.Integer(string="Mins")
