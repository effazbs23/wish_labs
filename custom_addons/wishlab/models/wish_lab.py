
from odoo import fields,models

class WishLab(models.Model):
    _name='wish.lab'
    _description='Wish Lab Model'

    name = fields.Char()
    email = fields.Char()
    connection_date = fields.Date()
    birthday = fields.Date()