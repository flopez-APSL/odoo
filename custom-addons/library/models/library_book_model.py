# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBook(models.Model):
    _name = 'library.book'

    name = fields.Char(string='Name')
    active = fields.Boolean('is Active?')
    image = fields.Binary()
    isbn = fields.Char(string='ISBN', size=13)
    description = fields.Html(string='Description')
    category_id = fields.Many2one('library.category', string='Category')




        

    




    