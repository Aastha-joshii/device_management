from odoo import models, fields, api


class Device_Management(models.Model):
    _name = "device.attribute"
    _description = "It has details of the devices attributes"
    _rec_name = 'name'

    name = fields.Char(string='Device Attribute Name')
    device_type_id = fields.Many2one('device.type', 'Device Type Id')
    required = fields.Boolean('isRequired?')
    device_attribute_value_id = fields.One2many('device.attribute.value', 'device_attribute_id', 'Device Attribute Value Id')

    _sql_constraints = [
        ('name_unique',
         'unique(name)',
         'Device name has to be unique')
    ]
