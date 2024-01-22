from odoo import models, fields, api


class Device_Management(models.Model):
    _name = "device.brand"
    _description = "It has details of the devices brands"
    _rec_name = 'name'

    name = fields.Char(string='Device Brand Name')
    device_model_ids = fields.One2many('device.model', 'device_brand_id','Device Model Id')

    _sql_constraints = [
        ('name_unique',
         'unique(name)',
         'Device name has to be unique')
    ]
