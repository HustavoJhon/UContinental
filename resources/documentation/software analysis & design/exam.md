# ANÁLISIS Y DISEÑO DE SOFTWARE  
## Actividad Semana #7 — Del Caos al Orden: Construyendo Requisitos y Casos de Uso

**Mgt. Ing. Melisa Betys Holguin Herrera**

---

# Parte 1: Análisis de Requisitos

A partir del caso de la tienda en línea, se clasificaron los 7 requerimientos originales y se propusieron 7 adicionales, totalizando 14 requisitos.

## 1.1 Requisitos Funcionales

| ID | Nombre del Requisito | Descripción |
|----|----------------------|-------------|
| RF-01 | Recuperación de contraseña | El sistema debe permitir al usuario recuperar su contraseña mediante un enlace seguro enviado al correo registrado. |
| RF-02 | Historial de compras | El sistema debe mostrar al cliente un listado detallado de sus compras anteriores. |
| RF-03 | Notificaciones por correo | El sistema debe enviar automáticamente un correo de confirmación tras una compra exitosa. |
| RF-04 | Gestión de stock | El sistema debe permitir al administrador consultar y actualizar inventario. |
| RF-05 | Búsqueda avanzada | El sistema debe ofrecer filtros por categoría, precio, valoración y disponibilidad. |
| RF-06 | Registro e inicio de sesión | El sistema debe permitir crear cuenta e iniciar sesión de forma segura. |
| RF-07 | Gestión del carrito de compras | El sistema debe permitir agregar, modificar y eliminar productos del carrito. |
| RF-08 | Procesamiento de pagos | El sistema debe integrar pasarelas de pago seguras. |
| RF-09 | Gestión de devoluciones | El sistema debe permitir solicitar devoluciones dentro del plazo establecido. |
| RF-10 | Catálogo de productos | El sistema debe mostrar productos con imágenes, descripción, precio y disponibilidad. |

---

## 1.2 Requisitos No Funcionales

| ID | Nombre del Requisito | Descripción |
|----|----------------------|-------------|
| RNF-01 | Compatibilidad responsive | El sistema debe adaptarse a móviles, tabletas y escritorio. |
| RNF-02 | Protección de datos | El sistema debe garantizar seguridad mediante cifrado SSL/TLS y normativas de privacidad. |
| RNF-03 | Rendimiento | El sistema debe responder en máximo 2 segundos. |
| RNF-04 | Disponibilidad | El sistema debe garantizar 99.5% de disponibilidad mensual. |

---

# Parte 2: Priorización con Método MoSCoW

| Prioridad | Significado |
|----------|-------------|
| M | Must Have (Obligatorio) |
| S | Should Have (Importante) |
| C | Could Have (Deseable) |
| W | Won't Have (No ahora) |

## Tabla de Priorización

| ID | Prioridad | Requisito |
|----|----------|-----------|
| RF-06 | M | Registro e inicio de sesión |
| RF-08 | M | Procesamiento de pagos |
| RF-01 | M | Recuperación de contraseña |
| RNF-02 | M | Protección de datos |
| RF-10 | M | Catálogo de productos |
| RF-07 | M | Gestión del carrito |
| RF-05 | S | Búsqueda avanzada |
| RF-03 | S | Notificaciones por correo |
| RF-04 | S | Gestión de stock |
| RNF-01 | S | Compatibilidad responsive |
| RF-02 | S | Historial de compras |
| RF-09 | C | Gestión de devoluciones |
| RNF-03 | C | Rendimiento |
| RNF-04 | W | Disponibilidad 99.5% |

---

# Parte 3: Identificación de Actores y Casos de Uso

## 3.1 Actores del Sistema

| Actor | Descripción | Tipo |
|------|-------------|------|
| Cliente | Usuario final que compra productos | Actor Primario |
| Administrador | Gestiona productos, stock y reportes | Actor Primario |
| Sistema de Correo | Envía notificaciones | Actor Secundario |
| Pasarela de Pago | Procesa pagos | Actor Secundario |

---

## 3.2 Casos de Uso

| Actor | Caso de Uso |
|------|-------------|
| Cliente | Registrarse |
| Cliente | Iniciar sesión |
| Cliente | Recuperar contraseña |
| Cliente | Buscar producto |
| Cliente | Agregar al carrito |
| Cliente | Realizar compra |
| Cliente | Ver historial de compras |
| Cliente | Solicitar devolución |
| Administrador | Gestionar inventario |
| Administrador | Gestionar productos |
| Administrador | Ver reportes de ventas |
| Sistema de Correo | Enviar confirmación |
| Pasarela de Pago | Procesar transacción |

---

# Parte 4: Relaciones de Casos de Uso

## Relaciones `<<include>>`

- Realizar compra `<<include>>` Procesar pago  
- Realizar compra `<<include>>` Enviar confirmación por correo  
- Realizar compra `<<include>>` Gestionar stock  

## Relaciones `<<extend>>`

- Iniciar sesión `<<extend>>` Recuperar contraseña  
- Buscar producto `<<extend>>` Filtrar categoría/precio  
- Ver historial `<<extend>>` Solicitar devolución  

---
																																																																																																																																	![[Pasted image 20260430111313.png]]
# Parte 5: Especificación Formal de Requisito

## RF-08 Procesamiento de Pagos en Línea

| Campo | Valor |
|------|------|
| ID | RF-08 |
| Nombre | Procesamiento de Pagos en Línea |
| Módulo | Compras / Checkout |
| Tipo | Funcional |
| Prioridad | Must Have |
| Versión | 1.0 |
| Fecha | Abril 2025 |
| Autor | Equipo de Análisis |

### Descripción

El sistema debe integrar al menos una pasarela de pago externa para procesar tarjetas de crédito, débito y billeteras digitales.

### Precondición

- Cliente autenticado  
- Producto en carrito  
- Dirección confirmada  

### Flujo Principal

1. Cliente accede al módulo de pago.  
2. Selecciona método de pago.  
3. Ingresa datos.  
4. Sistema valida con pasarela.  
5. Retorna aprobación o rechazo.  
6. Si aprueba: genera orden, descuenta stock y envía correo.  
7. Si rechaza: muestra error y permite reintentar.  

### Criterios de Aceptación

- Pago menor a 5 segundos  
- Correo en menos de 2 minutos  
- No almacenar datos de tarjeta  
- Error claro si falla  
- Orden registrada en historial  
- Descuento de stock solo si pago aprobado  

---

# Conclusión

El análisis permitió estructurar los requerimientos de la tienda en línea de forma organizada, clasificando requisitos funcionales y no funcionales.

El método MoSCoW facilitó priorizar funcionalidades críticas. Además, la identificación de actores y casos de uso permitió visualizar claramente las interacciones del sistema.