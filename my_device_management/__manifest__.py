# -*- coding: utf-8 -*-

{
    'name': 'My Device Management',
    'version': '1.0.0',
    'category': 'Device',
    'sequence': 5,
    'summary': 'Device Management',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/device_view.xml',
        'views/device_type_view.xml',
        'views/device_model_view.xml',
        'views/device_brand_view.xml',
        'views/device_attribute_view.xml',
        'views/device_attribute_value_view.xml',
        'views/device_attribute_assignment_view.xml',
        'views/device_assignment_view.xml',
        'views/employee_view.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {},
}
