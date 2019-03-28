# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class LibraryBook(models.Model):
    _name = 'library.book'

    name = fields.Char(string='Name')
    active = fields.Boolean('is Active?')
    image = fields.Binary()
    isbn = fields.Char(string='ISBN', size=13)
    description = fields.Html(string='Description')
    sales = fields.Integer(string="Sales", required=False, default=0)
    winner = fields.Char(compute='most_sold', string="Sales Record", readonly=True)
    category_id = fields.Many2one('library.category', string='Category')
    short_name = fields.Char('Short Title')
    author = fields.Many2one(comodel_name='library.author', string='Author')

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "{} ({})".format(record.name, record.author.name)))
        return result

    @api.depends('sales')
    def most_sold(self):
        controller = 0
        no_winner = 'No Bestseller'
        for record in self:
            if controller < record.sales:
                controller = record.sales
                record.winner = record.name
            else:
                record.winner = no_winner

    @api.constrains('name')
    def check_name(self):
        if not self.name:
            raise exceptions.ValidationError('Registre los campos obligatorios')

    @api.multi
    def action_library_book_information_author(self):
        return {
            "name": "Author Information",
            "view_type": "form",
            "view_mode": "form",
            "res_model": "library.author",
            "type": "ir.actions.act_window",
            "red_id": self.id,
        }
