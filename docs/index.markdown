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
- **Asignación de alérgenos a recetas y materia prima**: Cada receta y cada ingrediente se asocia a sus respectivos alérgenos, lo que permite crear una lista completa de alérgenos para los productos elaborados. Esto es especialmente útil para cumplir con regulaciones de salud y para la seguridad de los consumidores.
- **Generación de etiquetas de alérgenos**: Con la información de los ingredientes y los alérgenos asignados, el sistema permite generar etiquetas automáticas que cumplen con los estándares de etiquetado alimentario, asegurando la transparencia en la información proporcionada a los consumidores.

#### **♻️ Gestión de Sobras de Alimentos**
- **Control de sobras diarias**: Registra las sobras de alimentos no vendidos de cada día. El sistema calcula de manera automática el total de las sobras por semana, mes y año, permitiendo una visualización detallada del desperdicio de alimentos.
- **Análisis de desperdicio de materia prima**: A lo largo del tiempo, el sistema calcula el desperdicio de materia prima, brindando información valiosa para tomar decisiones sobre la compra y uso de ingredientes, mejorando así la eficiencia de los recursos.
- **Propuestas de producción optimizadas**: Con los datos históricos de las sobras, el sistema realiza sugerencias sobre la cantidad de producción para las semanas siguientes. Esto ayuda a minimizar las sobras y optimizar los recursos, ajustando la producción según la demanda real.

#### **💰 Cálculo de Coste de Producción**
- **Cálculo automático del coste de producción**: El sistema calcula el coste de producción de cada receta teniendo en cuenta el precio de la materia prima y el stock disponible. Esta funcionalidad permite tener un control preciso de los costos asociados a cada elaboración, ayudando a mantener los márgenes de ganancias.
- **Análisis de rentabilidad**: A partir de los datos del coste de producción, el sistema ofrece informes detallados que permiten identificar las recetas menos rentables y realizar ajustes en los precios o en la gestión de ingredientes para mejorar la rentabilidad.
- **Mejora en la toma de decisiones**: Con el análisis detallado de costes y márgenes de ganancia, el sistema ayuda a los gestores a tomar decisiones informadas sobre qué productos mantener en el menú, cuáles eliminar y cómo optimizar el uso de los recursos.

---

### **¿Qué hace único a este sistema?**
1. **Optimización en la gestión de ingredientes**: El sistema no solo facilita la creación de recetas, sino que también gestiona el uso eficiente de la materia prima, reduciendo el desperdicio y mejorando la rentabilidad.
2. **Visibilidad en el control de alérgenos**: Permite tener un control exhaustivo sobre los alérgenos presentes en cada receta e ingrediente, ayudando a cumplir con normativas y ofreciendo transparencia a los consumidores.
3. **Predicción y ajuste de producción**: Gracias a los datos históricos de sobras y desperdicio, el sistema ajusta la producción futura, minimizando las pérdidas y mejorando la eficiencia operativa.
4. **Análisis de costes y rentabilidad**: Ofrece herramientas avanzadas para calcular y analizar el coste de producción de cada receta, mejorando la toma de decisiones y los márgenes de ganancia.

---

### 🗺️ MAPA MÓDULO

El módulo se divide en dos secciones principales: **Producción** y **Sobras**. En la sección de **Producción**, los empleados responsables podrán añadir nuevas recetas, gestionar alérgenos y vincularlos con la materia prima correspondiente. Además, será posible incorporar y administrar dicha materia prima. Una vez guardada una receta, el sistema permitirá generar el etiquetado de alérgenos, elaborar informes de costes de producción y crear un producto a partir de la receta registrada.

Por otro lado, la sección de **Sobras** está destinada a la gestión de los desperdicios. En esta área se pueden añadir, editar y administrar las sobras, lo que facilita la generación de informes detallados y la creación de propuestas de producción basadas en los materiales disponibles.

<div style="text-align: center; margin: 20px;">
  <img src="img/mapa_obrador.png" alt="Mapa" style="width: 80%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>

--- 

### 🖼️ WIREFRAMES

#### Wireframe 01

<div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 20px;">
  <div style="flex: 1; margin-right: 20px; text-align: justify;">
	  El wireframe de la pestaña <strong>Producción</strong> muestra cómo se verá la página principal. Desde esta página se podrán crear recetas, añadir materia prima y alérgenos, así como gestionarlos de forma intuitiva. Además, ofrecerá la opción de generar el etiquetado correspondiente y un informe detallado de los costes de producción.
  </div>
  <div style="flex: 0 0 55%; text-align: center;">
	<img src="img/wireframe_recetario.png" alt="Wireframe producción" style="width: 100%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
  </div>
</div>

#### Wireframe 02

<div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 20px;">
  <div style="flex: 1; margin-right: 20px; text-align: justify;">  
	El wireframe de la pestaña <strong>Producción </strong>, en la función de <strong>Crear Recetas</strong>, ilustra cómo sería el proceso de creación de una receta y los datos que se solicitarán. Incluye secciones para alérgenos, ingredientes, tiempo de cocción, temperatura, entre otros detalles necesarios. Desde esta interfaz, será posible guardar la receta o guardar y proceder a crear un producto basado en ella.
  </div>
  <div style="flex: 0 0 55%; text-align: center;">
	<img src="img/wireframe_recetario_receta.png" alt="Wireframe producción" style="width: 100%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
  </div>
</div>

#### Wireframe 03

<div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 20px;">
  <div style="flex: 1; margin-right: 20px; text-align: justify;">  
	Aquí se muestra el wireframe de la pestaña <strong>Sobras</strong>, con una vista semanal de las sobras totales, que se puede visualizar por día, semana o mes. En esta pantalla se encuentra el botón de Informe de Sobras, desde el cual se pueden generar informes detallados sobre las sobras. Además, también se podrán consultar las propuestas de producción, las cuales ofrecen una estimación de las cantidades necesarias para optimizar la producción y evitar desperdicios.
  </div>
  <div style="flex: 0 0 55%; text-align: center;">
	<img src="img/wireframe_recetario_alergenos.png" alt="Wireframe producción" style="width: 100%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
  </div>
</div>


#### Wireframe 04

<div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 20px;">
  <div style="flex: 1; margin-right: 20px; text-align: justify;">  
	Aquí se muestra el wireframe de la pestaña <strong>Sobras</strong>, con una vista semanal de las sobras totales, que se puede visualizar por día, semana o mes. En esta pantalla se encuentra el botón de Informe de Sobras, desde el cual se pueden generar informes detallados sobre las sobras. Además, también se podrán consultar las propuestas de producción, las cuales ofrecen una estimación de las cantidades necesarias para optimizar la producción y evitar desperdicios.
  </div>
  <div style="flex: 0 0 55%; text-align: center;">
	<img src="img/wireframe_sobras_remanentes.png" alt="Wireframe producción" style="width: 100%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
  </div>
</div>


#### Wireframe 05

<div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 20px;">
  <div style="flex: 1; margin-right: 20px; text-align: justify;">  
	Aquí se muestra el wireframe de la pestaña <strong>Sobras</strong>, con una vista semanal de las sobras totales, que se puede visualizar por día, semana o mes. En esta pantalla se encuentra el botón de Informe de Sobras, desde el cual se pueden generar informes detallados sobre las sobras. Además, también se podrán consultar las propuestas de producción, las cuales ofrecen una estimación de las cantidades necesarias para optimizar la producción y evitar desperdicios.
  </div>
  <div style="flex: 0 0 55%; text-align: center;">
	<img src="img/wireframe_sobras_graficas.png" alt="Wireframe producción" style="width: 100%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
  </div>
</div>
---

### 🔄 DIAGRAMAS DE FLUJO

Aquí podemos observar los diferentes diagramas de flujo según la sección del módulo en la que nos encontremos. Comenzamos con el diagrama de **Producción**, donde se detallan las diversas funcionalidades del módulo y su flujo de trabajo. Se muestra cómo se pueden crear alérgenos, materia prima y recetas, y cómo estos elementos se integran para generar etiquetados e informes de producción.

<div style="text-align: center; margin: 20px;">
  <img src="img/diagrama_flujo_recetario.png" alt="Flowchart sobras" style="width: 70%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>

A continuación, se presenta el diagrama de la sección de **Sobras**, que ilustra el flujo de sus funcionalidades. Entre ellas se incluyen: añadir sobras, generar informes de propuestas de producción y de sobras, destacando cómo estas acciones se interrelacionan dentro del módulo.

<div style="text-align: center; margin: 20px;">
  <img src="img/diagrama_flujo_sobras.png" alt="Flowchart sobras" style="width: 70%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>

---
### <img src="img/image.png" alt="alt text" width="25" height="25"> ESQUEMA RELACIONAL DE LAS NUEVAS TABLAS

En este esquema relacional se muestra cómo se vinculan las nuevas tablas de la base de datos del módulo. Se puede observar que existen cinco tablas que interactúan entre sí según las acciones realizadas dentro del módulo, reflejando cómo los datos se conectan y se actualizan en función de las interacciones del usuario.

<div style="text-align: center; margin: 20px;">
  <img src="img/data_base_obrador1.png" alt="Esquema de la base de datos" style="width: 70%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>

---

### 🔒 CONTROL DE ACCESO

**Grupos de usuarios:**  
1. **Administradores**  
2. **Empleados** 
3. **Producción**
4. **Dependientas**   

**Acceso al módulo:**  
- **Todos los usuarios** tienen acceso al módulo en general.

**Accesos y permisos por grupo:**  
- **Administradores**  
	- Acceso completo a **Producción** y **Sobras**.
	- Permiso de **lectura y escritura** en todos los módulos, lo que les permite modificar y gestionar los datos de todos los registros.
- **Empleados**  
	- Acceso limitado a los apartados **Producción** y **Sobras**
	- Acceso de **lectura**, lo que les permitirá solo visualizar los dos apartados.
- **Producción**
	- Acceso limitado a **Producción** y **Sobras**.
	- Permiso de **lectura y escritura** a 'Producción'.
	- Permiso de **lectura** a 'Sobras'.
- **Dependientas**
	- Acceso limitado a los apartados **Producción** y **Sobras**.
	- Acceso de **lectura** al apartado de 'Producción'.
	- Acceso de **lectura y escritura** al de 'Sobras'.
