function listCars(cars) {
    return cars.map(car => car).join(', ');
}

function getCarByIndex(cars, index) {
    return cars[index];
}

module.exports = { listCars, getCarByIndex };