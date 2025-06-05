// async/await: Espera por una primesa
// es una forma de trabajar con promesas de manera más sencilla y legible.
// async : se coloca antes de la funcion y permite usar await dentro de ella.
// await : se coloca antes de una promesa y hace que el código espere hasta que la promesa se resuelva o se rechace.

// Ejemplo de uso de async/await
// function hervirAgua() {
//     return new Promise((resolve)=>{
//         console.log("Poniendo el agua a hervir...");
//         setTimeout(()=>{
//             resolve("El agua está lista para el café.");
//         }, 3000);
//     });
// }

// async function hacerCafe(){
//     console.log("Preparado para hacer café...");
//     const agua = await hervirAgua(); // Espera a que la promesa se resuelva
//     console.log(agua); // Imprime el mensaje una vez que el agua está lista
//     console.log("Agregando el café al agua...");
//     console.log("Café listo!");
// }

// hacerCafe(); // Llama a la función asíncrona para hacer café

// Ejemplo de varios await dentro de un funcion async

function validarPedido(pedidoId){
    return new Promise((resolve)=>{
        console.log(`Validando pedido con ID: ${pedidoId}...`);
        setTimeout(()=>{
            resolve(`Pedido ${pedidoId} validado.`);
        }, 2000);
    });
}

function notificarAlmacen(pedidoId){
    return new Promise((resolve)=>{
        console.log(`Notificando al almacén sobre el pedido ${pedidoId}...`);
        setTimeout(()=>{
            resolve(`Almacén notificado del pedido ${pedidoId}.`);
        }, 1000);
    });
}

function confirmarFinanzas(pedidoId){
    return new Promise((resolve)=>{
        console.log(`Confirmando a finanzas para el pedido ${pedidoId}...`);
        setTimeout(()=>{
            resolve(`Finanzas confirmadas para el pedido ${pedidoId}.`);
        }, 1500);
    });
}

async function procesarPedido(pedidoId) {
  console.log(`Iniciando el procesamiento del pedido ${pedidoId}...`);

  const validacion = await validarPedido(pedidoId); // Espera a que se valide el pedido
  console.log(validacion);

  const almacen = await notificarAlmacen(pedidoId); // Espera a que se notifique al almacén
  console.log(almacen);

  const confirmacion = await confirmarFinanzas(pedidoId); // Espera a que finanzas confirme
  console.log(confirmacion);

  console.log(`Pedido ${pedidoId} procesado exitosamente.`);
}

procesarPedido(12345) // Llama a la función asíncrona para procesar el pedido