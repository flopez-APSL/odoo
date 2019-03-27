# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBook(models.Model):
    _name = 'library.book'

    name = fields.Char(string='Name')
    active = fields.Boolean('is Active?')
    image = fields.Binary()
    isbn = fields.Char(string='ISBN', size=13)
    description = fields.Html(string='Description')
    sales = fields.Integer(string="Sales", required=False, default=0)
    winner = fields.Char(compute='mostsold', string="Sales Record", required=False)
    category_id = fields.Many2one('library.category', string='Category')
    short_name = fields.Char('Short Title')

    @api.depends('sales')
    def mostsold(self):
        controller = 0
        for record in self:
            if controller < record.sales:
                controller = record.sales
                winner = record.name
            else:
                pass
        
        return winner



    