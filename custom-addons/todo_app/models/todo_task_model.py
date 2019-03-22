from odoo import api, models, fields


class TodoTask(models.Model):
    _name = 'todo.task' # identificador del modelo para Odoo.
    _description = 'Aplicación de prueba'
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=False)
    user_id = fields.Many2one(
        'res.users',
        string='Responsible',
        default=lambda self: self.env.user)

    team_ids = fields.Many2many('res.partner', string='Team')

    @api.multi
    def do_clear_done(self):
        for task in self:
            task.active = False
        return True

    @api.multi
    def write(self, values):
        if 'active' not in values:
            values['active'] = True
        super().write(values)

    refers_to = fields.Reference([
        ('res.user', 'User'),
        ('res.partner', 'Partner')], 'Refers to')

    stage_fold = fields.Boolean(
        'Stage folded?',
        compute='_compute_stage_fold',
        # store=False the default
        search='_search_stage_fold',
        inverse='_write_stage_fold')

    # @api.depends('stage_id.Fold')
    # def _compute_stage_fold(self):
    #     for todo in self:
    #         todo.stage_fold = todo.stage_id.fold
    #
    # def _search_stage_fold(self, operator, value):
    #     return [('stage_id_.fold', operator, value)]
    #
    # def _write_stage_fold(self):
    #     for todo in self:
    #         todo.stage_id.fold = todo.stage_fold














