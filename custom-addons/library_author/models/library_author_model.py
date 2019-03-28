from odoo import models, fields, api


class LibraryAuthor(models.Model):
    _name = 'library.author'

    name = fields.Char('Author: ')
    active = fields.Boolean(default=True)
    country_id = fields.Many2one('res.country')
    book_ids = fields.Many2many('library.book', string="Books")
    book_id = fields.Many2one(comodel_name='library.book', string="Books")

    count_books = fields.Integer(compute='total_books', string="Total Books", readonly=True)

    @api.depends('book_ids')
    def total_books(self):
        for record in self:
            record.count_books = len(record.book_ids)
