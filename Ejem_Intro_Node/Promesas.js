// Promesa: son objetos que representan la finalización o el fracaso de una operación asíncrona.
// son una mejora sobre los callbacks, ya que permiten un manejo más limpio y estructurado de las operaciones asíncronas.
// tienen tres estados: pendiente, cumplida y rechazada.
// se crean utilizando el constructor `Promise` y se manejan con los métodos `then`, `catch` y `finally`.
// then se ejecuta cuando la promesa se cumple, catch se ejecuta cuando la promesa es rechazada y finally se ejecuta siempre, independientemente del resultado de la promesa.

// Ejemplo de Promesa
const promesaDePizza = new Promise((resolve, reject) => {
    let pizzaLista = false; // Simula que la pizza no está lista al inicio

    if (pizzaLista){
        resolve("La pizza está lista!"); // Resuelve la promesa si la pizza está lista
    }else{
        reject("No se pudo hacer la pizza"); // Rechaza la promesa si la pizza no está lista
    }
});

promesaDePizza
    .then((mensaje) => {
        console.log(mensaje); // Se ejecuta si la promesa se resuelve
    })
    .catch((error) => {
        console.error(error); // Se ejecuta si la promesa es rechazada
    })
    .finally(() => {
        console.log("Proceso de la pizza finalizado"); // Se ejecuta siempre, independientemente del resultado
    });