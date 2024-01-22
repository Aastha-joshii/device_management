from odoo import fields, models


class Device_Management(models.Model):
    _inherit = 'hr.employee'

    device_ids = fields.One2many('device.assignment', 'employee_id', string='Devices')
