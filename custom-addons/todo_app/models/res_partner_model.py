from odoo import api, models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    todo_ids = fields.Many2many('todo.task', string="To-do Teams", ondelete="cascade")
