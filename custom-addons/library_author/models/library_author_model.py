from odoo import models, fields


class LibraryAuthor(models.Model):
    _name = 'library.author'

    name = fields.Char('Author: ')
    active = fields.Boolean(default=True)
    country_id = fields.Many2one('res.country')
    # country_image = fields.Binary(related='country_id.image')  intento para coger un único campo de otro modelo.
