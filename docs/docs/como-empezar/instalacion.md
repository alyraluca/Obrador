---
layout: page
title: Instalación
menubar: config_menu
subtitle: Cómo empezar
show_sidebar: false
hero_image: ../../img/banner01.jpg 
hero_darken: true
---
### **Instalación**

## 1. Requisitos Previos  

Antes de instalar el módulo, recomendamos cumplir con los siguientes requisitos:  

- **Versión de Odoo:** Este módulo está desarrollado para Odoo **14**.  
- **Docker y Docker Compose:** La opción que recomendamos es o bine Docker Engine 24.0 con Docker Compose plugin >= 2.18.0; o bien Docker Desktop, ya que se ha desarrollado con la ayuda de estos.  
- **Dependencias:**  
  - Módulos relacionados: `mrp`, `product`. 

## 2. Instalación con docker
Si Odoo está funcionando en un contenedor Docker, sigue estos pasos:
1. Accede a la maquina donde está Odoo y entra en el contenedor:
     ```
    $ docker exec -it odoo_container bash
     ```

     ```
    $ /up.sh  ``` (si se utiliza el script de 'aoltra')
    
2. Descarga el módulo dentro del directorio de addons personalizado:
     ```
   $ git clone https://github.com/alyraluca/Obrador.git
    ```
3. Sal del contenedor y reinicia Odoo para que detecte el nuevo módulo
4. Desde la interfaz web de odoo:
   - Ir a Apps
   - Activar el Modo Desarrollador
   - Hacer click en 'Actualizar lista de Aplicaciones'
   - Buscar Obrador e instalarlo

## 3. Instalación sin docker
1. Descargar el módulo:
    ```
   $ git clone https://github.com/alyraluca/Obrador.git
    ```
2. Copiarlo en la carpeta de addons:
     ```
    $ mv obrador /odoo/custom/addons/
     ```
3. Actualizar la lista de módulos en Odoo:
   - Ir a Apps
   - Activar el Modo Desarrollador
   - Hacer click en 'Actualizar lista de Aplicaciones'
4. Reinicia Odoo (si es necesario)
   

