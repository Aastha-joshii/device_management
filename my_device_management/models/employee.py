import contextlib
from odoo import models, fields, api, sql_db, SUPERUSER_ID


class Device_Management(models.Model):
    _inherit = 'hr.employee'

    device_ids = fields.One2many('device.assignment', 'employee_id', string='Devices')

    def action_done(self):
        # res = super().action_confirm()
        connection = sql_db.db_connect('odoo17_school_mgm')
        with contextlib.closing(connection.cursor()) as cr:
            cr.autocommit(True)
            env = api.Environment(cr, SUPERUSER_ID, {})
            env['hr.employee'].create({'name': self.name})
