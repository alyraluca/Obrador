# -*- coding: utf-8 -*-
{
    'name': "produccion_mod2",

    'summary': "Creación de recetas""
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': "Creación de recetas, lista de alergenos presentes en los productos y sobras de alimentos del dia no vendidos.""
        Long description of module's purpose
    "Creación de recetas a partir de nuestro inventario de materia prima comprada.
Cada producto final creado tendrá una lista de alergenos.
Lista de sobras por dia, semana, mes. De está manera se podrá mejorar la producción, reducir las sobras y ahorrar recursos y materia prima. TAB (Recetas)
Lista de productos de creación propia organizados por: categoria.
Botton de crear receta/producto: o Ingredientes (se puede escoger de la lista de materia prima que tendremos almacenado en los otros modulos.) o Cantidad: cada ingrediente tendrá la cantidad especificada TAB (Alergenos)
Lista alergenos
Botton NUEVO alergeno: donde podremos añadir nuevos alergenos.
Tenemos una vista por lista de alergenos y otra vista por tabla de alergenos junto con los productos TAB(Sobras)
Vemos una lista (que se puede organizar por dia, semana o mes) con las sobras.
Hay in botton de NUEVO, donde se puede poner las sobras de ese día de alimentos perecederos."",

    'author': "Alexandra Raluca, Savu",
    'website': "https://github.com/alyraluca/produccion_mod2",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
