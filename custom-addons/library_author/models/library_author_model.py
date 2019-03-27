from odoo import models, fields, api


class LibraryAuthor(models.Model):
    _name = 'library.author'

    name = fields.Char('Author: ')
    active = fields.Boolean(default=True)
    country_id = fields.Many2one('res.country')
    # country_image = fields.Binary(related='country_id.image')  intento para coger un único campo de otro modelo.

    book_ids = fields.Many2many('library.book', string="Books")

    count_books = fields.Integer(compute='total_books', string="Total Books")

    @api.depends('book_ids')
    def total_books(self):
        for record in self:
            record.count_books = len(record.book_ids)
