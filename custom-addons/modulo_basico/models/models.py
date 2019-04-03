# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ModuloFields(models.Model):
    _name = 'modulo.fields'
    _description = 'Fields'

    name = fields.Char('Crea un formulario, y nómbralo: ')
    fieldchar = fields.Char('Char')
    booleano = fields.Boolean(string="Boolean")
    fieldfloat = fields.Float(string="Float",  required=False, )
    integerfield = fields.Integer(string="Integer", required=False, )
    fielddate = fields.Date(string="Date", required=False,)
    fielddatetime = fields.Datetime(string="Date Time", required=False, )
    fieldhtml = fields.Html(string="Campo html",)
    fieldtext = fields.Text(string="Texto", required=False, )
    fieldchoose = fields.Selection(string="Selection: ", selection=[('a', 'Opción 1'), ('b', 'Opción 2'), ], required=False, )

    @api.depends('FIELDS_NAMES')
    def _compute_amount(self):
        """
        @api.depends() should contain all fields that will be used in the calculations.
        """
        pass


class NewModule(models.Model):
    _name = 'modulo.relacional'
    _inherit = 'sale.order'

    name = fields.Char('Campos Relacionales')










