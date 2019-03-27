from odoo import models, fields, api, exceptions


class Library_Book_Date(models.Model):
    _inherit = 'library.book'

    date = fields.Date(string='Release Date')

    @api.onchange('date')
    def onchange_date(self):             # mensaje de error.
        today = fields.Date.today()
        if self.date  > today:
            raise exceptions.UserError(
                'Date should be less than today')

