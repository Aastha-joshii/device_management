from odoo import models, fields


class Device_Management(models.Model):
    _name = "device.attribute.assignment"
    _description = "It has details of the devices attribute assignments"
    _rec_name = 'device_id'

    device_id = fields.Many2one('device.device', 'Device Id')
    device_attribute_id = fields.Many2one('device.attribute', 'Device Attribute Id')
    device_attribute_value_id = fields.Many2one('device.attribute.value', 'Device Attribute Value Id')

    _sql_constraints = [
        ('name_unique',
         'unique(device_id,device_attribute_id)',
         'Device name has to be unique')
    ]
