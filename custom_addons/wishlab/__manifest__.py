{
    'name': 'Wish Labs',
    'version': '1.0.0',
    'depends': ['base','mail'],
    'author': 'BRAIN STATION 23',
    'description': """
        A module to store birthdays and automatically wish the users through mail.
    """,
    'data': [
        'security/ir.model.access.csv',
        'data/wish_lab_cron.xml',
        'data/mail_server.xml',
        'views/wish_lab_views.xml',
        'views/wish_lab_menu.xml'
    ],
    'application': True,
    'installable': True,
}
