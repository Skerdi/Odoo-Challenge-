{
    'name': 'Rain Measurements',
    'version': '1.0',
    'category': 'Tools',
    'author': 'Keti Hysi',
    'application' : 'Ture',
    'summary': 'Tool to measure the amount of rain that has fallen during the day.',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/rain_measurements_menu.xml',
        'views/rain_measurements_views.xml',
        'views/url_saved_records_view.xml',
    ]
}