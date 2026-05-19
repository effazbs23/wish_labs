from odoo import fields, models, api
import datetime as dt


class WishLab(models.Model):
    _name = 'wish.lab'
    _description = 'Wish Lab Model'

    partner_id = fields.Many2one('res.partner', string="Partner ID")
    name = fields.Char(related="partner_id.name")
    email = fields.Char(related="partner_id.email")
    connection_date = fields.Datetime(related="partner_id.create_date")
    birthday = fields.Date()

    @api.model
    def _wish_handler(self):
        partners = self.search([])
        today = dt.date.today()
        for record in partners:
            try:
                with self.env.cr.savepoint():
                    if record.connection_date:
                        conn_date = fields.Date.to_date(record.connection_date)
                        if conn_date.month == today.month and conn_date.day == today.day:
                            print(f"Anniversary with : {record.name} -> Sending email to {record.email}")
                    if record.birthday:
                        bday = fields.Date.to_date(record.birthday)
                        if bday.month == today.month and bday.day == today.day:
                            print(f"Birthday of : {record.name} -> Sending email to {record.email}")
            except Exception as e:
                print(f"Error while sending wishes to {record.name} ID : {record.id}")
                print("str(e)")
                continue
