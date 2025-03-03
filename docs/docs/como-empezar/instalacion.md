---
layout: page
title: Instalación
menubar: config_menu
subtitle: Cómo empezar
show_sidebar: false
hero_image: ../../img/banner01.jpg 
hero_darken: true
---
## **Instalación**

### **1. Requisitos Previos**  

Antes de instalar el módulo, recomendamos cumplir con los siguientes requisitos:  

- **Versión de Odoo:** 
    - Este módulo está desarrollado para Odoo **14**.

- **Docker y Docker Compose:** 
    - Docker Engine **24.0** con Docker Compose plugin >= **2.18.0** (Recomendada ya que se ha desarrollado con estas configuraciones). 
    - O bien **Docker Desktop**.
  
- **Dependencias:**  
    - Módulos requeridos: **`mrp`**, **`product`**.
  
- **Revisar antes de instalar:**
    - Si usas Docker, asegúrate de que Odoo esté corriendo en un contenedor.  
    - Si instalas sin Docker, comprueba que Odoo tenga acceso a la carpeta de addons.

### **2. Instalación con docker**
Si Odoo está funcionando en un contenedor Docker, sigue estos pasos:

**Paso 1: Accede al contenedor de Odoo**
Ejecuta el siguiente comando en tu terminal:

     ``` bash
    $ docker exec -it odoo_container bash
     ```
Si se utiliza el script de **'aoltra'**, ejecuta:

    ``` 
    $ /up.sh 
    ```

**Paso 2: Descarga el módulo**
Ubicaté en el directorio de addons personalizados y clona el repositorio:

     ``` 
    $ git clone https://github.com/alyraluca/Obrador.git
     ```

**Paso 3: Reinicia Odoo**

Sal del contenedor y reinicia Odoo

**Paso 4: Instalar el módulo y activarlo**
Desde la interfaz web de Odoo:
   - Ir a Apps
   - Activar el Modo Desarrollador
   - Hacer click en 'Actualizar lista de Aplicaciones'
   - Buscar Obrador e instalarlo

### 3. Instalación sin docker

**Paso 1: Descargar el módulo**

    ``` 
    $ git clone https://github.com/alyraluca/Obrador.git
    ```

**Paso 2: Copiarlo en la carpeta de addons**

    ``` 
    $ mv obrador /odoo/custom/addons/
    ```

**Paso 3: Actualizar la lista de módulos en Odoo**
   - Ir a Apps
   - Activar el Modo Desarrollador
   - Hacer click en 'Actualizar lista de Aplicaciones'
  
**Paso 4: Reinicia Odoo**

    ``` 
    $ systemctl restart odoo
    ```
   

