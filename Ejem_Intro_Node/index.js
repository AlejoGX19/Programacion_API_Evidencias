console.log("Hola, Node.js!");

// Ejemplo del Event Loop en Node.js
// Esto muestra cómo Node.js maneja las operaciones asíncronas(tiempos de espera) y el Event Loop.

console.log("Inicio del Event Loop");
setTimeout(() => {
    console.log("Esto se ejecuta después de 2 segundos");
}, 2000 );

setTimeout(() => {
    console.log("Esto se ejecuta después de 0 segundo, pero después del inicio del Event Loop");
}, 0 );

console.log("Fin del Event Loop");