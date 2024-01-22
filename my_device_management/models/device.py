from odoo import models, fields


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
