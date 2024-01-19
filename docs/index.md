
# Producción Modulo 2

NOMBRE: producción

DESCRIPCIÓN
Creación de recetas, lista de alergenos presentes en los productos y sobras de alimentos del dia no vendidos.

### DESCRIPCIÓN DETALLADA

-	Creación de recetas a partir de nuestro inventario de materia prima comprada.
-	Cada producto final creado tendrá una lista de alergenos.
-	Lista de sobras por dia, semana, mes. De está manera se podrá mejorar la producción, reducir las sobras y ahorrar recursos y materia prima.
TAB (Recetas)
-	Lista de productos de creación propia organizados por: categoria.
-	Botton de crear receta/producto:
o	Ingredientes (se puede escoger de la lista de materia prima que tendremos almacenado en los otros modulos.)
o	Cantidad: cada ingrediente tendrá la cantidad especificada
TAB (Alergenos)
-	Lista alergenos
-	Botton NUEVO alergeno: donde podremos añadir nuevos alergenos.
-	Tenemos una vista por lista de alergenos y otra vista por tabla de alergenos junto con los productos
TAB(Sobras)
-	Vemos una lista (que se puede organizar por dia, semana o mes) con las sobras.
-	Hay in botton de NUEVO, donde se puede poner las sobras de ese día de alimentos perecederos.

### MAPA MODULO 2

![mapa__module2.jpg](img/mapa__module2.jpg)

### DEPENDENCIAS DE OTROS MODULOS

Modulo 2 depende de: Compras, Ventas. Necesitamos la lista de productos/ingredientes del modulo de ‘Compas’. También necesitamos la lista de productos que vendemos del modulo de ‘Ventas’.

### WIREFRAME

Wireframe de la TAB de ‘Recetas’.

![wireframe_recetas1.jpg](img/wireframe_recetas1.jpg)

Wireframe del TAB de ‘Recetas’ de la función de ‘Crear Recetas’.

![wireframe_recetas2.jpg](img/wireframe_recetas2.jpg)

Wireframe del TAB de ‘Alergenos’ con vista en forma de tabla.

![wireframe_alergenos1.jpg](img/wireframe_alergenos1.jpg)

Wireframe del TAB de ‘Alergenos’ con vista en forma de lista.

![wireframe_alergenos2.jpg](img/wireframe_alergenos2.jpg)

Wireframe del TAB de ‘Alergenos’ de la función de ‘Nueva receta’.

![wireframe_alergenos3.jpg](img/wireframe_alergenos3.jpg)

Wireframe del TAB de ‘Sobras’ con la vista de lista.

![wireframe_sobras1.jpg](img/wireframe_sobras1.jpg)

Wireframe del TAB de ‘Sobras’ con la función de ‘Nuevas Sobras’.

![wireframe_sobras2.jpg](img/wireframe_sobras2.jpg)

### CONTROL DE ACCESO

Grupos: administradores, empleados.
Acceso al modulo: todos los usuarios
Administradores: acceso a ‘Recetas’, ‘Alergenos’ y ‘Sobras’.
	- Permiso de lectura y escritura a todos los modulos.
Empleados: acceso a ‘Recetas’, ‘Alergenos’ y ‘Sobras’.
	- Permiso de lectura y escritura a ‘Recetas’, ‘Alergenos’ y ‘Sobras’.

### DIAGRAMAS DE FLUJO

Diagrama de flujo del TAB de ‘Recetas’

![flowchart_recetas.jpg](img/flowchart_recetas.jpg)

Diagrama de flujo del TAB de ‘Alergenos’

![flowchart_alergenos.jpg](img/flowchart_alergenos.jpg)

Diagrama de flujo del TAB de ‘Sobras’

![flowchart_sobras.jpg](img/flowchart_sobras.jpg)

### ESQUEMA RELACIONAL DE LAS NUEVAS TABLAS

![data_base_module2.jpg](img/data_base_module2.jpg)


### CARACTERISTICAS COMUNICACIÓN

Modulo 2: comunica con compras y ventas.
Requisitos: acceso a la lista de materia prima del modulo de ‘Compras’ y acceso a los productos que vendemos del modulo de ‘Ventas’.
Protocolo/ Formato del mensaje: podemos utilizar RPC (es una llamada remota a procedimientos para invocar funciones de otros módulos) o también podemos hacer uso de una base de datos compartida.
Estructura Mensaje RPC:


                module1/models/module1_model.py
                from odoo import models, api
                class Module1Model(models.Model):
                    _name = 'module1.model'

                    @api.model
                    def call_remote_function(self, data):
                        module2_model = self.env['module2.model']
                        result = module2_model.process_data_remotely(data)
                        # Procesar el resultado si es necesario
                        return result



