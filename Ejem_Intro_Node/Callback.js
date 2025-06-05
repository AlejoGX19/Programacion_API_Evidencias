// Callback: son funciones que se pasan como argumentos a otras funciones y se ejecutan después de que la función principal ha terminado su tarea.

// function pedirPizza(callback) {
//     console.log("Pedido de pizza en proceso...");
//     setTimeout(() => {
//         console.log("La pizza está lista!");
//         callback();
//     }, 2000); // Simula un tiempo de espera de 2 segundos
// }

// function comerPizza() {
//     console.log("Ahora puedo comer la pizza...");
// }

// pedirPizza(comerPizza);

//---------------------------------------------------------------------


// Mas de un ejemplo de Callback como argumento a otra función 

function verificarCandidato(nombre, callbackAceptar, callbackRechazar) {
    console.log(`Verificando al candidato: ${nombre}...`);
    
    const cumple = Math.random() > 0.5; // Simula una verificación aleatoria
    if (cumple) {
        callbackAceptar(nombre); // Llama al callback de aceptación
    }else {
        callbackRechazar(nombre); // Llama al callback de rechazo
    }
}

// Definimos los callbacks
function aceptarCandidato(nombre){
    console.log(`${nombre} ha sido aceptado. Se procede con la oferta`);
}

function rechazarCandidato(nombre){
    console.log(`${nombre} no cumple con los requisitos. Se notifica el rechazo`);
}

// Llamamos a la función con los callbacks
verificarCandidato("Juan Perez", aceptarCandidato, rechazarCandidato); 