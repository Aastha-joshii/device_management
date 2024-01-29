import contextlib
import psycopg2
from odoo import models, fields, api, sql_db, SUPERUSER_ID


class Device_Management(models.Model):
    _inherit = 'hr.employee'

    device_ids = fields.One2many('device.assignment', 'employee_id', string='Devices')

    def action_done(self):
        conn = sql_db.db_connect('odoo17_school_mgm')
        with contextlib.closing(conn.cursor()) as cr:
            cr._cnx.autocommit = True
            env = api.Environment(cr, SUPERUSER_ID, {})
            env['hr.employee'].create({'name': self.name, 'mobile_phone': self.mobile_phone, 'work_phone': self.work_phone})

