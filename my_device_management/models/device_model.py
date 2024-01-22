from odoo import models, fields, api


class Device_Management(models.Model):
    _name = "device.model"
    _description = "It has details of the devices models"
    _rec_name = 'name'

    name = fields.Char(string='Device Model Name')
    device_type_id = fields.Many2one('device.type', 'Device Type Id')
    device_brand_id = fields.Many2one('device.brand', 'Device Brand Id')


    _sql_constraints = [
        ('name_unique',
         'unique(name,device_type_id,device_brand_id)',
         'Device name and code has to be unique')
    ]
