function calculateAverage(ages) {
    if (ages.length === 0) return 0;
    const total = ages.reduce((sum, age) => sum + age, 0);
    return total / ages.length;
}

module.exports = { calculateAverage };