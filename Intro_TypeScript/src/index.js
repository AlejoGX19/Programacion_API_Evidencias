"use strict";
// setTimeout(function(): void {
//     console.log('Hello, TypeScript! desde función anónima (TS)');
// }, 1000);
Object.defineProperty(exports, "__esModule", { value: true });
// const sumar = (a: number, b: number): number => a + b;
// console.log(sumar(5, 10)); // 15
//Callback
// function saludar(nombre: string, callback: () => void): void {
//     console.log(`Hola ` + nombre + `!`);
//     callback();
// }
// // Llamada a la función saludar
// saludar('Juan', function(): void {
//     console.log('¡Bienvenido!');
// });
//  async function obtenerDatos(): Promise<void> {
//     const data =  await fetch(`https://jsonplaceholder.typicode.com/todos/`);
//     const json = await data.json();
//     console.log(json);
//  }
// Llamada a la función obtenerDatos
// obtenerDatos().then((): void => {
//     console.log('Datos obtenidos correctamente');
// }).catch((error): void => {
//     console.error('Error al obtener los datos:', error);
// });
// Ejemplo de promesa
// const promesa: Promise<string> = new Promise((resolve, reject) => {
//     setTimeout(() => ('Hecho'), 1000);
// });
// promesa.then(console.log);
// // Ejemplo de funcion flecha con parametros rest
// const suma = (...numeros: number[]): number => numeros.reduce((a,b) => a + b);
// console.log(suma(1, 2, 3, 4, 5)); // 15
//Interfaces,  actua como una clase
// interface Usuario {
//     nombre: string;
//     edad: number;
// }
// const usuario: Usuario = {nombre: 'Juan', edad: 30};
// console.log(usuario.nombre); // Juan
// console.log(usuario.edad); // 30
const Modulo_1 = require("./Modulo");
console.log(`El valor de PI es: ${Modulo_1.PI}`);
