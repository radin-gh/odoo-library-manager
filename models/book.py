from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    author = fields.Char()
    isbn = fields.Char(string='ISBN')
    available = fields.Boolean(default=True)