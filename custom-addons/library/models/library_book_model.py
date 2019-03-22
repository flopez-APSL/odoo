# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBook(models.Model):
    name = fields.Char(string='Name')
    active = fields.Boolean('is Active?')
    image = fields.Binary()
    pages = fields.Integer(string='# pages')
    isbn = fields.Char(string='ISBN', size=13)


