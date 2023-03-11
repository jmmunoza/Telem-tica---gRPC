# **Miniproyecto Microservicios (Python y Nodejs)**
*******

**Tabla de Contenido**

1. [Arquitectura](#arquitectura)
2. [Microservicio de Inventario](#inventario)
3. [Microservicio de Órdenes](#orden)
4. [Microservicio de Pago](#pago) 
5. [Api](#api) 
6. [Ejecución](#ejecution)
7. [Ejemplos](#ejemplos)<br>

*******

<div id='arquitectura'/> 

### **1. Arquitectura**
![Microservices](https://user-images.githubusercontent.com/69641274/224455152-7805b0e0-3d49-4ba9-9d97-5ec5d2d6b5f2.jpg)

Antes de comenzar a hablar de cada uno de los componentes en específico, es necesario echar un vistazo general de todo el sistema. Lo primero que se notan son dos enormes cajas: Client side y Backend side.

Por el lado de Client Side, se trata del entorno en el cual el cliente interactúa con la solución. En esta solución solamente requiere de un computador, ya sea de escritorio o portatil, y el aplicativo Postman. Postman será el intermediario entre el usuario y el sistema, ya que este brinda gran variedad de peticiones HTTP como GET, POST, PUT, DELETE, entre muchas otras, algo que no ofrece un Browser convencional, el cual solamente provee las peticiones GET. Cabe recalcar que Postman no es la única solución, existe gran cantidad de herramientas similares como Thunder Client (extensión de VSCode) o Katalon Studio. Postman envia sus peticiones HTTP por medio de Internet y llegan hasta el API que permite redireccionar dichas peticiones hasta cada uno de los microservicios.

Por el lado de Backed Side, se trata de todo el gran sistema en sí. Aquí se encuentran los tres microservicios y el API que permite la conexión a estos por parte del usario. De forma práctica, cada uno de estos componentes se trata de un aplicativo de software. Cada una de estas piezas de código se encuentran ejecutando en 4 máquinas virtuales distintas. El elegido para proveer dichas máquinas se trata de Amazon Web Services, medianete su servicio de máquina EC2. Los componentes al interior se comunican todos por medio de gRPC, el cual está soportado sobre HTTP2. Como se puede ver, los componentes se encuentran interconectados entre sí, pero no de forma bidireccional. Esta bidireccionalidad será explicada a fondo más abajo.

Puede que el lector se esté cuestionando la falta de un componente de Frontend Side. Este, por motivos prácticos, ha sido descartado en la implementación del proyecto debido a que no se ajusta con los objetivos del reto. 


*******

<div id='inventario'/> 

### **2. Microservicio de Inventario**

El servicio de inventario alberga todos los productos que el usuario podrá ver y comprar. El servicio ofrece la posibilidad de añadir un producto (add()), obtener uno por medio de su ID (get()), eliminar uno por medio de su ID (get()), actualizar uno (update()) u obtener todos los productos disponibles en la "base de datos".
Un producto cuenta con los siguientes atributos:
* Nombre
* Identificador
* Precio
* Stock

Este servicio se encuentra implementado en Python y se encuentra ligado a los demás componentes, aunque este no se puede comunicar directamente a ellos. No puede enviar solicitudes a Órdenes o a Pagos. El servicio no cuenta con una base de datos, pero si hace una simulación de esta con datos en memoria. La desventaja es que cada vez que se cierra el proceso, se reinician los valores a cero.

A continuación, su archivo .proto:

```js
syntax = "proto3";

service InventoryService {
    rpc getAll(GetAllProductsRequest) returns (stream Product) {}
    rpc add(AddProductRequest)        returns (Product) {}
    rpc get(GetProductRequest)        returns (Product) {}
    rpc delete(DeleteProductRequest)  returns (ProductResponse) {}
    rpc update (Product)              returns (ProductResponse) {}
}

message Product {
    string product_id = 1;
    string name       = 2;
    float price       = 3;
    int32 stock       = 4;
}

message AddProductRequest {
    string name = 1;
    float price = 2;
    int32 stock = 3;
}

message GetAllProductsRequest {
}

message ProductResponse {
    bool is_successful  = 1;
    string message      = 2;
}

message GetProductRequest {
    string product_id = 1;
}

message DeleteProductRequest {
    string product_id = 1;
}
```

*******

<div id='orden'/> 

### **3. Microservicio de Órdenes**

El servicio de órdenes es hasta cierto grado similar al de inventario. Puedes crear órdenes (create()), obtener una orden (get()), obtener todas (getAll()), cancelarla (cancel()) o completarla (complete()). Una orden se compone de los siguientes atributos.

* Identificador de la orden
* Identificador del producto a comprar
* Cantidad de productos a comprar

El servicio se encuentra igualmente programado en Python. Este se puede comunicar al servicio de inventario para hacer uso principalmente de las funciones get() y delete(). Al igual que como pasa con todos los servicios, la base de datos es inexistente. Solamente hay datos en memoria que se pierden cada vez que se para la ejecución del programa.

Este es el archivo .proto de órdenes:

```js
syntax = "proto3";

service OrderManagementService {
    rpc getAll(GetAllOrdersRequest)  returns (stream Order) {}
    rpc get(OrderRequest)            returns (Order) {}
    rpc create(CreateOrderRequest)   returns (Order) {}
    rpc cancel(OrderRequest)         returns (OrderResponse) {}
    rpc complete(OrderRequest)       returns (OrderResponse) {}
}

message Order {
    string order_id    = 1;
    string product_id  = 2;
    int32 amount       = 3;
}

message GetAllOrdersRequest {
}

message CreateOrderRequest {
    string product_id = 1;
    int32 amount      = 2;
}

message OrderResponse {
    bool is_successful = 1;
    string message     = 2;
}

message OrderRequest {
    string order_id = 1;
}
```

*******

<div id='pago'/>  

### **4. Microservicio de Pago**

El servicio de pagos, el más complejo de todos, se trata de una simulación de pasarela de pagos en donde el usuario paga y completa así sus órdenes. Con el servicio puedes crear un usuario (createUser), añadir fondos a su cuenta (addMoney()), obtener al usuario (getUser()) o pagar una orden (payOrder()).

Por un lado, el usuario se compone de los siguientes atributos:
* Identificador
* Nombre
* Fondos en la cuenta

Por el otro, un pago cuenta con los siguientes atributos:
* Identificador de la orden
* Identificador del usuario
* Monto del pago

Este servicio se encuentra desarrollado en NodeJS y tampoco cuenta con base de datos. Hace uso tanto de los servicios de inventario, para obtener productos, como de orden, para obtener y completar ordenes.

A continuación, el archivo .proto:

```js
syntax = "proto3";

service PaymentService {
    rpc payOrder (Payment) returns (PaymentResponse) {}
    rpc addMoney (AddMoneyRequest) returns (PaymentResponse) {}
    rpc createUser (CreateUserRequest) returns (User) {}
    rpc getUser (UserRequest) returns (User);
}

message Payment {
    string order_id = 1;
    string user_id  = 2;
    float amount    = 3;
}

message User {
    string user_id = 1;
    string name    = 2;
    float balance  = 3;
}

message PaymentResponse {
    bool is_successful = 1;
    string message      = 2;
}

message CreateUserRequest {
    string name = 1;
}

message AddMoneyRequest {
    string user_id = 1;
    float amount   = 2;
}

message UserRequest {
    string user_id = 1;
}
```

*******

<div id='api'/>  

### **5. API**

La API, el intermediario entre el usuario y los servicios. Esta se encuentra desarrollada en NodeJS y hace uso de Express para poder hacer el enrutamientos de las solicitudes y convertirlas de HTTP a un llamado de método remoto con gRPC y HTTP2.

Este componente tiene acceso a los tres microservicios, pero estos no pueden hacer uso de esta. Para el enrutamiento, se cuentan con tres secciones:
* /inventory para el servicio de inventario
* /orders para el servicio de órdenes
* /payment para el servicio de pagos


#### **5.1. Métodos de inventario:**
Para hacer uso de los métodos del servicio de inventario, se cuentan con las siguientes rutas

* **get():** para llamar a este método se hace por medio del método HTTP GET y de la ruta:

```sh
 /inventory/get/{identificador}
```

* **getAll():** para llamar a este método se hace por medio del método HTTP GET y de la ruta:

```sh
 /inventory/getall
```

* **add():** para llamar a este método se hace por medio del método HTTP POST y de la ruta:
```sh
 /inventory/add/
```

El body de la solicitud es el siguiente:
```js
{
    "name" : "Hammer",
    "price" : 215.5,
    "stock": 3
}
```
El método retornará un JSON similar, pero con un campo adicional, el identificador del producto.

* **delete():** para llamar a este método se hace por medio del método HTTP DELETE y de la ruta:
```sh
 /inventory/delete/
```

El body de la solicitud es el siguiente:
```js
{
    "product_id" : "3afa59c7-a390-4b32-ad36-d625d92ed418"
}
```
El método retornará un JSON similar al siguiente en caso de éxito.

```js
{
    "is_successful" : true,
    "message" : "The product was deleted successfully"
}
```
En caso de error, se retornará el siguiente JSON.

```js
{
    "is_successful" : false,
    "message" : "There was an error"
}
```


* **update():** para llamar a este método se hace por medio del método HTTP POST y de la ruta:
```sh
 /inventory/update/
```

El body de la solicitud es el siguiente:
```js
{
    "product_id" : "3afa59c7-a390-4b32-ad36-d625d92ed418",
    "name" : "Hammer",
    "price" : 24.5,
    "stock": 3
}
```

El método buscará el producto con el mismo identificador y los actualizará. Posteriormente, retornará un JSON similar al siguiente en caso de éxito.

```js
{
    "is_successful" : true,
    "message" : "The product was updated successfully"
}
```
En caso de error, se retornará el siguiente JSON.

```js
{
    "is_successful" : false,
    "message" : "There was an error"
}
```

#### **5.2. Métodos de órdenes:**
Para hacer uso de los métodos del servicio de órdenes, se cuentan con las siguientes rutas

* **get():** para llamar a este método se hace por medio del método HTTP GET y de la ruta:

```sh
 /orders/get/{identificador}
```

* **getAll():** para llamar a este método se hace por medio del método HTTP GET y de la ruta:

```sh
 /orders/getall
```

* **create():** para llamar a este método se hace por medio del método HTTP POST y de la ruta:
```sh
 /orders/create/
```

El body de la solicitud es el siguiente:
```js
{
    "product_id" : "3afa59c7-a390-4b32-ad36-d625d92ed418",
    "amount" : 45
}
```

El método retornará un JSON similar, pero con un campo adicional, el identificador de la orden.

* **cancel():** para llamar a este método se hace por medio del método HTTP POST y de la ruta:
```sh
 /orders/cancel/
```

El body de la solicitud es el siguiente:
```js
{
    "order_id" : "85d8ec54-784b-4b0a-8ebb-29174bb72210",
}
```

El método buscará el producto con el mismo identificador y los eliminará. Posteriormente, retornará un JSON similar al siguiente en caso de éxito.

```js
{
    "is_successful" : true,
    "message" : "The order was cancelled successfully"
}
```
En caso de error, se retornará el siguiente JSON.

```js
{
    "is_successful" : false,
    "message" : "There was an error"
}
```

* **complete():** para llamar a este método se hace por medio del método HTTP POST y de la ruta:
```sh
 /orders/complete/
```

El body de la solicitud es el siguiente:
```js
{
    "order_id" : "85d8ec54-784b-4b0a-8ebb-29174bb72210",
}
```

El método buscará el producto con el mismo identificador y los eliminará, y de paso descontará el stock del producto asociado haciendo uso del servicio de inventarios (aunque esta última parte no fue implementada por temas de tiempo, solamente elimina la orden). Posteriormente, retornará un JSON similar al siguiente en caso de éxito.

```js
{
    "is_successful" : true,
    "message" : "The order was completed successfully"
}
```
En caso de error, se retornará el siguiente JSON.

```js
{
    "is_successful" : false,
    "message" : "There was an error"
}
```

#### **5.3. Métodos de pago:**
Para hacer uso de los métodos del servicio de pago, se cuentan con las siguientes rutas

* **createUser():** para llamar a este método se hace por medio del método HTTP POST y de la ruta:
```sh
 /payment/createuser/
```

El body de la solicitud es el siguiente:
```js
{
    "name" : "Juan Manuel",
}
```

El método retornará un JSON similar, pero con dos campos adicionales, el identificador del usuario y sus fondos.
```js
{
    "user_id" : "c24c4391-83a6-4805-9e58-9007795a4cfd":,
    "name" : "Juan Manuel",
    "balance" : 0
}
```

* **addMoney():** para llamar a este método se hace por medio del método HTTP POST y de la ruta:
```sh
 /payment/addmoney/
```

El body de la solicitud es el siguiente:
```js
{
    "user_id" : "Juan Manuel",
    "amount": 15004.5
}
```

El método retornará un mensaje de confirmación en caso de que el proceso sea exitoso.

```js
{
    "is_successful" : true,
    "message" : "Money added successfully"
}
```
En caso de error, se retornará el siguiente JSON.

```js
{
    "is_successful" : false,
    "message" : "There was an error"
}
```

* **getUser():** para llamar a este método se hace por medio del método HTTP GET y de la ruta:

```sh
 /payment/getuser/{identificador}
```

* **payOrder():** para llamar a este método se hace por medio del método HTTP POST y de la ruta:
```sh
 /payment/payorder/
```

El body de la solicitud es el siguiente:
```js
{
    "order_id" : "85d8ec54-784b-4b0a-8ebb-29174bb72210",
    "user_id" : "c24c4391-83a6-4805-9e58-9007795a4cfd",
    "amount" : 14999.9
}
```

El método retornará un mensaje de confirmación en caso de que el proceso sea exitoso.

```js
{
    "is_successful" : true,
    "message" : "Money added successfully"
}
```
En caso de error, que se puede dar porque el stock no es suficiente o el monto de dinero es innecesario (es por esto que pagos llama a inventario y ordenes), se retornará un JSON con el mensaje de error específico.

```js
{
    "is_successful" : false,
    "message" : "There was an error"
}
```

*******

<div id='ejecution'/>  

### **6. Ejecución**

Cada componente cuenta con una carpeta en donde se encuentra un archivo main.py o main.js, el cual es el que se ejecuta para correr cada servidor. Para ser capaz de ejecutar todo, se requiere instalar librerías para permitir la ejecución de Python y NodeJS en la máquina.

Lo principal, lo que debe correrse siempre en un inicio.

```sh
 $ sudo apt-get update
 $ sudo apt-get upgrade
```

Ahora es necesario instalar Python y pip.

```sh
 $ sudo apt-get install python3
 $ sudo apt-get install python3-pip
```

Instale las librerias requeridas para gRPC y dotenv.

```sh
 $ sudo python3 -m pip install grpcio
 $ sudo python3 -m pip install grpcio-tools
 $ sudo python3 -m pip install dotenv
```

Para instalar NodeJS.

```sh
$ sudo curl -fsSL https://deb.nodesource.com/setup_19.x | sudo -E bash - && sudo apt-get install -y nodejs
```

Ahora el entorno está preparado para ser ejecutado. Para correr códigos de Python se llama al siguiente comando.

```sh
$ sudo python3 main.py
```

Para correr los códigos de NodeJS se llama al siguiente comando.

```sh
$ sudo node main.js
```

*******


<div id='ejemplos'/> 

### **7. Ejemplos**

A continuación, algunas capturas mostrando el funcionamientos de la aplicación.

* Añadiendo un producto
![image](https://user-images.githubusercontent.com/69641274/224460679-c4d481f5-3e7f-4715-ae7d-c91497b99f35.png)

* Obteniendo todos los productos
![image](https://user-images.githubusercontent.com/69641274/224460699-fdee196f-c4a8-4035-ae62-56860601ce5c.png)

* Eliminando un producto
![image](https://user-images.githubusercontent.com/69641274/224460716-3ea9a174-3722-4348-8ffe-c3b016b133b9.png)

* Creando una orden
![image](https://user-images.githubusercontent.com/69641274/224460737-f44ea071-a8ca-45af-9e9a-a16ef4458ea9.png)

* Obteniendo todas las órdenes
![image](https://user-images.githubusercontent.com/69641274/224460755-798fb6f3-1ffc-451b-a518-17ed1cc36edf.png)

* Creando un usuario
![image](https://user-images.githubusercontent.com/69641274/224460769-8b0e24db-15dc-49c8-aa04-8eae38c35a07.png)

* Pagando una orden con dinero insuficiente
![image](https://user-images.githubusercontent.com/69641274/224460853-c1c20535-26c1-4533-9d57-6e36bc47217d.png)

* Pagando la orden con dinero suficiente
![image](https://user-images.githubusercontent.com/69641274/224460884-0413692d-1c6f-4118-8453-35a5a31ce392.png)

* Los tres servicios corriendo desde la terminal
![image](https://user-images.githubusercontent.com/69641274/224461030-0c592e40-5e7e-4cfb-aafd-de8c851aa5eb.png)



*******










