---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
title: Obrador
subtitle: Gestión de recetas, alergenos y sobras de alimentos
hero_image: img/banner01.jpg 
hero_darken: true
---
### **FUNCIONALIDADES DESTACADAS**

#### **📝 Creación y Gestión de Recetas**
- **Elaboración de recetas personalizadas**: Utiliza el stock de materia prima disponible para crear recetas adaptadas a las necesidades de producción. El sistema permite agregar ingredientes, cantidades y métodos de preparación de forma sencilla.
- **Asignación de alérgenos a recetas**: Cada receta y cada ingrediente se asocia a sus respectivos alérgenos, lo que permite crear una lista completa de alérgenos para los productos elaborados. Esto es especialmente útil para cumplir con regulaciones de salud y para la seguridad de los consumidores.
- **Generación de etiquetas de alérgenos**: Con la información de los ingredientes y los alérgenos asignados, el sistema permite generar etiquetas automáticas que cumplen con los estándares de etiquetado alimentario, asegurando la transparencia en la información proporcionada a los consumidores.

#### **♻️ Gestión de Sobras de Alimentos**
- **Control de sobras diarias**: El sistema calcula de manera automática el total de las sobras por semana, mes y año, gracias a las ventas (TPV) y la producción del día a día (Producción), permitiendo una visualización detallada del desperdicio de alimentos.
- **Análisis de desperdicio de materia prima**: A lo largo del tiempo, el sistema calcula el desperdicio de materia prima, brindando información valiosa para tomar decisiones sobre producción, mejorando así la eficiencia de los recursos.
- **Propuestas de producción optimizadas**: Con los datos históricos de las sobras, el sistema realiza sugerencias sobre la cantidad de producción para las semanas siguientes. Esto ayuda a minimizar las sobras y optimizar los recursos, ajustando la producción según la demanda real.

---

### **¿Qué hace único a este sistema?**
1. **Optimización en la gestión de ingredientes**: El sistema no solo facilita la creación de recetas, sino que también gestiona el uso eficiente de la materia prima, reduciendo el desperdicio y mejorando la rentabilidad.
2. **Visibilidad en el control de alérgenos**: Permite tener un control exhaustivo sobre los alérgenos presentes en cada receta, ayudando a cumplir con normativas y ofreciendo transparencia a los consumidores.
3. **Predicción y ajuste de producción**: Gracias a los datos históricos de sobras y ventas, el sistema ajusta la producción futura, minimizando las pérdidas y mejorando la eficiencia operativa.

---

### 🗺️ MAPA MÓDULO

El módulo se divide en dos secciones principales: **Recetario** y **Sobras**. En la sección de **Recetario**, los empleados encargados podrán añadir nuevas recetas y gestionar alérgenos. También será posible incorporar materia prima, la cual se importará desde **'Inventario'**. Una vez guardada una receta, el sistema generará automáticamente el etiquetado de alérgenos e ingredientes. Además, los usuarios del módulo de **'Producción'** podrán utilizar las recetas directamente en sus 'órdenes de producción'.

Por otro lado, la sección de **Sobras** está enfocada en la gestión de desperdicios. En esta área, los usuarios podrán visualizar y administrar las sobras, lo que facilitará la generación de informes detallados y la creación de propuestas de producción basadas en las sobras calculadas a partir de las ventas del módulo de TPV y la producción del módulo de **'Producción'**. También será posible visualizar esta información a través de gráficos, mejorando la interpretación y el análisis de los datos.

<div style="text-align: center; margin: 20px;">
  <img src="img/" alt="Mapa" style="width: 80%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>

--- 

### 🖼️ WIREFRAMES

#### Wireframe 01

<div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 20px;">
  <div style="flex: 1; margin-right: 20px; text-align: justify;">
	  El wireframe de la pestaña <strong>Recetario</strong> muestra cómo estará organizada la página principal y las opciones disponibles. Desde ahí se podrán crear recetas nuevas añadiendo la materia prima, los alérgenos y la categoría que corresponda. Además, será posible enlazar las recetas con el módulo de <strong>Producción</strong>, para que se puedan usar directamente en las órdenes de producción y registrar automáticamente cuánto se ha fabricado y en qué fecha. También incluirá la opción de generar etiquetas para los productos y descargar las recetas en formato Excel, ya sea todas o solo las que se necesiten. La idea es que esta página haga más fácil gestionar las recetas y conectarlas con otros módulos del sistema.
  </div>
  <div style="flex: 0 0 55%; text-align: center;">
	  <img src="img/wireframe_recetario.png" alt="Wireframe recetario" style="width: 100%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
  </div>
</div>

#### Wireframe 02

<div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 20px;">
  <div style="flex: 1; margin-right: 20px; text-align: justify;">  
	El wireframe de la pestaña <strong>Recetario</strong>, en la función de <strong>Crear Recetas</strong>, muestra cómo sería el proceso para crear una receta y los datos que se van a pedir. Tendrá secciones para añadir alérgenos, seleccionándolos de una lista disponible, y para los ingredientes, que estarán enlazados con el módulo de <strong>Inventario</strong>, lo que facilitará tener a mano la lista de materia prima. También incluirá campos para indicar el tiempo de cocción, la temperatura y otros detalles importantes. Desde esta misma interfaz se podrá guardar la receta de manera sencilla.
  </div>
  <div style="flex: 0 0 55%; text-align: center;">
	  <img src="img/wireframe_recetario_receta.png" alt="Wireframe producción" style="width: 100%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
  </div>
</div>

#### Wireframe 03

<div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 20px;">
  <div style="flex: 1; margin-right: 20px; text-align: justify;">  
	Este es el wireframe de la pestaña <strong>Alérgenos</strong>, diseñada para gestionar y añadir alérgenos de manera sencilla. Desde aquí se podrán registrar todos los alérgenos necesarios, que luego podrán utilizarse al crear recetas. Junto al nombre de cada alérgeno, habrá una columna que indicará en cuántos productos está presente. Además, esta página permitirá generar etiquetas de alérgenos, mostrando en qué productos se encuentran, lista para imprimir y compartir con futuros clientes.
  </div>
  <div style="flex: 0 0 55%; text-align: center;">
	  <img src="img/wireframe_recetario_alergenos.png" alt="Wireframe producción" style="width: 100%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
  </div>
</div>


#### Wireframe 04

<div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 20px;">
  <div style="flex: 1; margin-right: 20px; text-align: justify;">  
	Este es el wireframe de la subpestaña <strong>Remanentes</strong>, ubicada dentro de la pestaña <strong>Sobras</strong>. Los datos de esta sección se actualizarán automáticamente, considerando las órdenes de producción del día registradas en el módulo de Producción y las ventas del módulo de TPV al cierre de caja. Aquí será posible visualizar la información filtrada por despachos, fechas o incluso por producto. Además, esta subpestaña ofrecerá la opción de generar informes detallados con todos los datos y crear una "Propuesta de producción". Esta última funcionalidad permitirá que el sistema, basándose en patrones históricos, sugiera producciones estratégicas para reducir desperdicios y optimizar las ventas.
  </div>
  <div style="flex: 0 0 55%; text-align: center;">
	  <img src="img/wireframe_sobras_remanentes.png" alt="Wireframe producción" style="width: 100%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
  </div>
</div>


#### Wireframe 05

<div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 20px;">
  <div style="flex: 1; margin-right: 20px; text-align: justify;">  
	Este es el wireframe de la pestaña <strong>Sobras</strong>, en el apartado <strong>Gráficas</strong>. Aquí se presenta toda la información recopilada en la pestaña anterior, organizada de manera visual y más fácil de interpretar mediante gráficos. Podremos analizar datos de ventas, producción y sobras (calculadas automáticamente) de forma individual o combinada, lo que permitirá comparar y entender mejor las diferencias entre estos aspectos. Además, será posible filtrar la información por despacho, producto, fecha o categoría de producto. El sistema ofrecerá varios tipos de gráficos y permitirá descargarlos en distintos formatos, así como generar informes completos con todos estos datos para facilitar su análisis y distribución.
  </div>
  <div style="flex: 0 0 55%; text-align: center;">
	  <img src="img/wireframe_sobras_graficas.png" alt="Wireframe producción" style="width: 100%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
  </div>
</div>
---

### 🔄 DIAGRAMAS DE FLUJO

Aquí podemos observar los diferentes diagramas de flujo según la sección del módulo en la que nos encontremos. Comenzamos con el diagrama de **Recetario**, donde se detallan las diversas funcionalidades del módulo y su flujo de trabajo. Se muestra cómo se pueden crear alérgenos y recetas, y cómo estos elementos se integran para generar etiquetados e informes de producción.

<div style="text-align: center; margin: 20px;">
  <img src="img/diagrama_flujo_recetario.png" alt="Flowchart sobras" style="width: 70%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>

A continuación, se presenta el diagrama de la sección de **Sobras**, que ilustra el flujo de sus funcionalidades. Entre ellas se incluyen: generar informes de propuestas de producción y de sobras, destacando cómo estas acciones se interrelacionan dentro del módulo y como también, podemos visualizar los gráficos con esta información.

<div style="text-align: center; margin: 20px;">
  <img src="img/diagrama_flujo_sobras.png" alt="Flowchart sobras" style="width: 70%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>

---
### <img src="img/image.png" alt="alt text" width="25" height="25"> ESQUEMA RELACIONAL DE LAS NUEVAS TABLAS

En este esquema relacional se muestra cómo se vinculan las nuevas tablas de la base de datos del módulo. Se puede observar que existen siete tablas que interactúan entre sí según las acciones realizadas dentro del módulo. Podemos ver resaltado son amarillo, tablas de otros modulos que importaremos y útilizaremos para poder, por ejemplo, calcular las sobras de nuestros productos. Enlazaremos el modulo de 'Producción', el del 'Inventario' y el del TPV.

<div style="text-align: center; margin: 20px;">
  <img src="img/data_base_obrador1.png" alt="Esquema de la base de datos" style="width: 70%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>

---

### 🔒 CONTROL DE ACCESO

**Grupos de usuarios:**  
1. **Administradores**  
2. **Empleados** 
3. **Dependientas**   

**Acceso al módulo:**  
- **Todos los usuarios** tienen acceso al módulo en general.

**Accesos y permisos por grupo:**  
- **Administradores**  
	- Acceso completo a **Recetario** y **Sobras**.
	- Permiso de **lectura y escritura** en todos los módulos, lo que les permite modificar y gestionar los datos de todos los registros.
- **Empleados**  
	- Acceso limitado a los apartados **Recetario** y **Sobras**
	- Acceso de **lectura**, lo que les permitirá solo visualizar los dos apartados.
- **Dependientas**
	- Acceso limitado a los apartados **Recetario** y **Sobras**.
	- Acceso de **lectura** al apartado de 'Recetario' y al de 'Sobras'.


---

#### Enlace repositorio
[github.com/alyraluca/Obrador](https://github.com/alyraluca/Obrador)