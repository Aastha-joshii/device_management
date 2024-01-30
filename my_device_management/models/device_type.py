from odoo import models, fields, api


class Device_Management(models.Model):
    _name = "device.type"
    _description = "It has details of the devices types"
    _rec_name = 'name'

    name = fields.Char(string='Device Name')
    code = fields.Boolean('isShared?')
    sequence_number = fields.Char('Sequence Number')
    device_attribute_ids = fields.One2many('device.attribute', 'device_type_id', 'Device Attribute Id')
    device_model_ids = fields.One2many('device.model', 'device_type_id', 'Device Model Id')
    device_ids = fields.One2many('device.device', 'device_type_id', 'Device Id')

    _sql_constraints = [
        ('name_unique',
         'unique(name,code)',
         'Device name and code has to be unique')
    ]

    @api.model
    def create(self, vals_list):
        vals_list['sequence_number'] = self.env['ir.sequence'].next_by_code('device.type.code')
        return super(Device_Management, self).create(vals_list)
