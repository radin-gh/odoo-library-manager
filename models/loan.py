from datetime import timedelta

from odoo import api, fields, models
from odoo.exceptions import UserError


class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Library Loan'

    book_id = fields.Many2one('library.book', string='Book', required=True)
    borrower_id = fields.Many2one('res.partner', string='Borrower', required=True)
    loan_date = fields.Date(default=fields.Date.today, required=True)
    due_date = fields.Date(
        default=lambda self: fields.Date.today() + timedelta(days=14),
        required=True,
    )
    return_date = fields.Date(readonly=True)
    state = fields.Selection(
        [('borrowed', 'Borrowed'), ('returned', 'Returned')],
        default='borrowed',
    )
    late_days = fields.Integer(compute='_compute_late_days')

    @api.depends('due_date', 'return_date')
    def _compute_late_days(self):
        today = fields.Date.today()
        for loan in self:
            end = loan.return_date or today
            loan.late_days = max((end - loan.due_date).days, 0) if loan.due_date else 0

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            book = self.env['library.book'].browse(vals.get('book_id'))
            if not book.available:
                raise UserError('This book is already borrowed.')
        loans = super().create(vals_list)
        loans.mapped('book_id').write({'available': False})
        return loans

    def action_return(self):
        for loan in self:
            loan.write({'state': 'returned', 'return_date': fields.Date.today()})
            loan.book_id.available = True