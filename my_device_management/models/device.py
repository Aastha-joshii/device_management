from odoo import models, fields, api, sql_db, SUPERUSER_ID
import contextlib


class Device_Management(models.Model):
    _name = "device.device"
    _description = "It has details of the devices"
    _rec_name = 'name'

    name = fields.Char(string='Device Name')
    shared = fields.Boolean('isShared?')
    device_type_id = fields.Many2one('device.type', 'Device Type Id')
    device_brand_id = fields.Many2one('device.brand', 'Device Brand Id')
    device_model_id = fields.Many2one('device.model', 'Device Model Id')
    attributes = fields.One2many('device.attribute.assignment', 'device_id', 'Attributes')

    _sql_constraints = [
        ('name_unique',
         'unique(name)',
         'Device name has to be unique')
    ]

    # def create(self, vals):
    #     connection = sql_db.db_connect('odoo17_school_mgm')
    #     with contextlib.closing(connection.cursor()) as cr:
    #         cr._cnx.autocommit = True
    #         env = api.Environment(cr, SUPERUSER_ID, {})
    #         env['device.device'].create({'name': self.name})
