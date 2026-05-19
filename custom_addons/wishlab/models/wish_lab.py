
from odoo import fields,models

class WishLab(models.Model):
    _name='wish.lab'
    _description='Wish Lab Model'

    partner_id = fields.Many2one('res.partner',string="Partner ID")
    name = fields.Char(related="partner_id.name")
    email = fields.Char(related="partner_id.email")
    connection_date = fields.Datetime(related="partner_id.create_date")
    birthday = fields.Date()