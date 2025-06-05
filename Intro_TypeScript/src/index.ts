// setTimeout(function(): void {
//     console.log('Hello, TypeScript! desde función anónima (TS)');
// }, 1000);

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

// import { PI } from './Modulo';
// console.log(`El valor de PI es: ${PI}`);

// Ejemplo de clase y herencia
// class Animal {
//     constructor(public nombre: string) {}
    
//     hacerSonido(): void {
//         console.log(`${this.nombre} hace un sonido.`);
//     }
// }


class Usuario {
    constructor(
        public id: number,
        public nombre: string,
        public correo: string,
        public password: string,
        public telefono: string
    ) {}
}

class Producto {
    constructor(
        public id: number,
        public nombre: string,
        public precio_inicial: number,
        public precio_final: number ,
        public usuario: Usuario  // Relación con la clase Usuario (FK)
    ) {}
}