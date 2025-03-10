---
layout: page
menubar: config_menu
title: Instalación y Configuración
show_sidebar: false
hero_image: img/banner01.jpg 
hero_darken: true
---
## **Instalación**

### **1. Requisitos Previos**  

Antes de instalar el módulo, recomendamos cumplir con los siguientes requisitos: 

- **Versión de Odoo:** 
    - Este módulo está desarrollado para Odoo **`14`**.

- **Docker y Docker Compose:** 
    - Docker Engine 24.0 con Docker Compose plugin >= 2.18.0 (Recomendada ya que se ha desarrollado con estas configuraciones). 
    - O bien Docker Desktop.
  
- **Dependencias:**  
    - Módulos requeridos: **`mrp`**, **`product`**.
  
- **Revisar antes de instalar:**
    - Si usas Docker, asegúrate de que Odoo esté corriendo en un contenedor.  
    - Si instalas sin Docker, comprueba que Odoo tenga acceso a la carpeta de addons.

### **2. Instalación con docker**
Si Odoo está funcionando en un contenedor Docker, sigue estos pasos:

**Paso 1:** Accede al contenedor de Odoo

Ejecuta el siguiente comando en tu terminal:

```
$ docker exec -it odoo_container bash
```

Si se utiliza el script de **`aoltra`**, ejecuta:

``` 
$ /up.sh 
```

**Paso 2:** Descargamos el módulo en addons

``` 
$ git clone https://github.com/alyraluca/Obrador.git
```

**Paso 3:** Reiniciamos el contenedor

**Paso 4:** Instalamos el módulo

   - Nos colocamos en la interfaz web de Odoo
   - Ir a Apps
   - Activar el Modo Desarrollador
   - Hacer click en 'Actualizar lista de Aplicaciones'
   - Buscar Obrador e instalarlo

### 3. Instalación sin docker

**Paso 1:** Descargar el módulo

``` 
$ git clone https://github.com/alyraluca/Obrador.git
```

**Paso 2:** Copiarlo en la carpeta de addons

``` 
$ mv obrador /odoo/custom/addons/
```

**Paso 3:** Actualizar la lista de módulos en Odoo
   - Ir a Apps
   - Activar el Modo Desarrollador
   - Hacer click en 'Actualizar lista de Aplicaciones'
   - Instalamos módulo
  
**Paso 4:** Reinicia Odoo

``` 
$ systemctl restart odoo
```
   


