import contextlib
from odoo import models, api, sql_db, SUPERUSER_ID
class SaleOrder(models.Model):
   _inherit = 'sale.order'
   def action_confirm(self):
       res = super().action_confirm()
       connection = sql_db.db_connect('odoo17_school_mgm')
       with contextlib.closing(connection.cursor()) as cr:
           cr.autocommit(True)
           env = api.Environment(cr, SUPERUSER_ID, {})
           sale_order = env['sale.order'].search([])
           print(sale_order)
