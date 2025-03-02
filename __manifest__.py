# -*- coding: utf-8 -*-
{
    'name': "Obrador",

    'summary': """
        Creación de recetas, control de elergenos y sobras""",

    'description': """
        Creación de recetas a partir del stock de materia prima y asignación de alergenos, tanto a las recetas como a la materia prima. Con la información de los alergenos y materia prima, se podrá crear etiquetado para los productos elaborados.
	Añadir las sobras del día y como consecuencia se calculará automaticamente, en un informe, las sobras totales de la semana, mes o año.
    """,

    'author': "Alexandra Raluca, Savu",
    'website': "https://github.com/alyraluca/Obrador",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Obrador',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'mrp'],

    'application': True,

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/receta_report.xml',
        'reports/receta_etiqueta.xml',
        'reports/sobras_report.xml',
        'data/demo/data_alergenos.xml',
        'data/demo/data_productos.xml',
        'data/demo/data_receta.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
