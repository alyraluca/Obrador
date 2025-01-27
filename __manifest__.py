# -*- coding: utf-8 -*-
{
    'name': "Obrador",

    'summary': """
        Creación de recetas, control de elergenos y sobras""",

    'description': """
        Creación de recetas a partir del stock de materia prima y asignación de alergenos, tanto a las recetas como a la materia prima. Con la información de los alergenos y materia prima, se podrá crear etiquetado para los productos elaborados.
	Añadir las sobras del día y como consecuencia se calculará automaticamente las sobras totales de la semana, mes o año, además de calcular el desperdicio de materia prima a lo largo del tiempo.
	Con las sobras de todas las semanas, el sistema, propondrá una cantidad de producción para las semanas siguientes para asi poder minimizar las sobras.
	Con la información del stock de materia prima, junto con el precio, se nos calculará el coste de producción de cada elaboración. Esto nos ayudará a mejorar nuestro marjen de ganancias, además de poder ver donde estamos perdinedo dinero y recursos.
    """,

    'author': "Alexandra Raluca, Savu",
    'website': "https://github.com/alyraluca/Obrador",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'application': True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
