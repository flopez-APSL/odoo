from odoo import fields, models, api


class NewModule(models.Model):
    _inherit = 'todo.task'

    new_field_id = fields.Many2one(comodel_name="res.users", string="Responsible", required=False, )
    date_deadline = fields.Date('Dateline')

