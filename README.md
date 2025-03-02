# Obrador

### Modulo de Obrador para proyecto final de modulo de SGE 2024/2025

# URLs
- [Repositorio de GitHub](https://github.com/alyraluca/Obrador)
- [GitHub - Page](https://alyraluca.github.io/Obrador/)

# Orden de instalación
El módulo depende de los módulos `product` y `mrp`, los cuales se instalarán automáticamente una vez instalado el nuestro.

# Listado de módulo.modelo
### Heredamos o utilizamos:
- `product.product` (heredamos)
- `product.template` (heredamos)
- `mrp.production` (referenciamos)

### Nuestros módulo.modelo:
- `obrador.recetas`
- `obrador.alergenos`
- `obrador.remanentes`
- `obrador.receta.ingrediente`
- `obrador.graficas`

# Acceso a empleados
### Datos de autenticación del administrador:
- **Usuario:** `nie`
- **Contraseña:** `root`

Hemos creado un grupo de acceso para el módulo, llamado `Obrador`, para facilitar las asignaciones de los permisos de nuestros empleados.

Posteriormente, tenemos 3 niveles de permisos para 3 tipos de roles:
1. **Management**: acceso total al módulo.
2. **Cocinero/Panadero**: permisos de lectura y escritura en `recetas`, `alergenos` y `graficas`, pero solo pueden leer la parte de `sobras`.
3. **Vendedor**: permisos de lectura y escritura en `sobras` y `graficas`, pero solo pueden leer `recetas` y `alergenos`.

Los ajustes para asignar estos roles se encontrarán en la configuración de cada usuario en Odoo.

# Data
Tenemos en la carpeta `data/demo` tres ficheros que se cargarán automáticamente al instalar el módulo. Contienen:
- Datos de alérgenos.
- Varias materias primas para añadir a las recetas.
- Varios productos para los cuales poder crear recetas.
- Un ejemplo de cómo quedaría una receta.
