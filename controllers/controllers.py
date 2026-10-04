# from odoo import http


# class LibraryManager(http.Controller):
#     @http.route('/library_manager/library_manager', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_manager/library_manager/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_manager.listing', {
#             'root': '/library_manager/library_manager',
#             'objects': http.request.env['library_manager.library_manager'].search([]),
#         })

#     @http.route('/library_manager/library_manager/objects/<model("library_manager.library_manager"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_manager.object', {
#             'object': obj
#         })

