{
    'name': 'Library Manager',
    'version': '1.0',
    'summary': 'Manage books and loans',
    'category': 'Services',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_views.xml',
        'views/loan_views.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}