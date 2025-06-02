function isAdult(age) {
    const ageParameter = 18;
    return age >= ageParameter ? "Eres un Adulto." : "Eres un Niño.";
}

module.exports = { isAdult };