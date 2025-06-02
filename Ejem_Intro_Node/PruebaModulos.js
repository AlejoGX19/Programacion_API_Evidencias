const { isAdult } = require('./Modulo_Edad');
const { listCars, getCarByIndex } = require('./ModuloAutos');
const { calculateAverage } = require('./ModuloPromedioEdad');

console.log(isAdult(20)); // "Eres un Adulto."
console.log(listCars(["Toyota", "Honda", "Ford"])); // "Toyota, Honda, Ford"
console.log(getCarByIndex(["Toyota", "Honda", "Ford"], 2)); // "Ford"
console.log(calculateAverage([20, 30, 40])); // 30