
from odoo import fields,models,api
import datetime as dt

class WishLab(models.Model):
    _name='wish.lab'
    _description='Wish Lab Model'

    partner_id = fields.Many2one('res.partner',string="Partner ID")
    name = fields.Char(related="partner_id.name")
    email = fields.Char(related="partner_id.email")
    connection_date = fields.Datetime(related="partner_id.create_date")
    birthday = fields.Date()

    @api.model
    def _wish_handler(self):
        partners = self.search([])
        for record in partners:
            try:
                with self.env.cr.savepoint():
                    if(record.connection_date.date() == dt.date.today()):
                        print(f"Anniversary with : {record.name} -> Sending email to {record.email}")
                    pass
            except Exception as e:
                print(f"Error while sending wishes to {record.name} ID : {record.id}")
                print("str(e)")
                continue