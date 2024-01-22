from odoo import models, fields, api


class Device_Management(models.Model):
    _name = "device.attribute.value"
    _description = "It has details of the devices attributes values"
    _rec_name = 'name'

    name = fields.Char(string='Device Attribute Value Name')
    device_attribute_id = fields.Many2one('device.attribute', 'Device Attribute Id')

    _sql_constraints = [
        ('name_unique',
         'unique(name,device_attribute_id)',
         'Device name has to be unique')
    ]
