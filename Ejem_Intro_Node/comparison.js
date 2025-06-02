// Uso del sistema de modulos de node.js require, moule.exports y exports, import
// Modulos nativos de node.js fs, path, http, os, events, etc.

// const fs = require('fs');

// console.log("Inicio de la lectura del archivo");
// fs.readFile('archivo.txt', 'utf8', (err, data) => {
//     if (err) throw err;
//     console.log("Contenido del archivo:", data);
// });
// console.log("Fin de la lectura del archivo");


// Tener instalada la libreria chalk npm install chalk
(async () => {
    const chalk = await import('chalk');

    console.log(chalk.default.blue('Hola, Node.js!'));
    console.log(chalk.default.red.bold('Hasta luego, Node.js!'));
})();