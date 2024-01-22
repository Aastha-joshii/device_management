from odoo import models, fields


class Device_Management(models.Model):
    _name = "device.assignment"
    _description = "It has details of the devices assignments"
    _rec_name = 'name'

    name = fields.Char(string='Device Name')
    device_id = fields.Many2one('device.device', 'Device Id')
    employee_id = fields.Many2one('hr.employee', 'Employee Id')
    start_date = fields.Date('Start Date')
    expire_date = fields.Date('Expire Date')
    state = fields.Selection(
        [('new', 'New'), ('draft', 'Draft'), ('approve', 'Approve'), ('return', 'Returned'), ('reject', 'Rejected')],
        default='new', string='Status')

    _sql_constraints = [
        ('name_unique',
         'unique(name)',
         'Device name has to be unique')
    ]

    def create_draft(self):
        self.state = 'draft'

    def action_approve(self):
        self.state = 'approve'

    def action_return(self):
        self.state = 'return'

    def action_reject(self):
        self.state = 'reject'
