# coding: utf-8
from odoo import models, fields, api, _

class BatchItems(models.Model):
    _name = "batch.items"
    _rec_name = "batch_name"

    batch_code = fields.Char(string='Batch Code')
    batch_name = fields.Char(string='Batch Name')



class BatchProcessing(models.Model):
    _name = "batch.processing"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    batch_id = fields.Many2one('batch.items', string='Batch')
    batch_qty = fields.Float(string='Quantity')
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street 2')
    zip = fields.Char(string='Zip', change_default=True)
    city = fields.Char(string='city')
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict')
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
