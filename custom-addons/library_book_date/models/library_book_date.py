from odoo import models, fields


class Library_Book_Date(models.Model):
    _inherit = 'library_book'

    date = fields.Date(string='Release Date')
    
