// const parametroEstatura = 1.30,
// cosnt parametroPeso = 100,
// const parametroEstadoCivil = "Soltero",

function mostrarMensajeIfAnimado(){
    var estatura = parseInt(document.getElementById("estatura").value);
    var peso = parseFloat(document.getElementById("peso").value);
    var estadoCivil = document.getElementById("estadoCivil").value;

    const parametroEstatura = 1.30;
    const parametroPeso = 100;
    const parametroEstadoCivil = "Soltero";

    //If Aninado
    if (estatura >= parametroEstatura) {
        if (peso <= parametroPeso) {
            if (estadoCivil === parametroEstadoCivil) {
                resultado = "Saludable"
            } else {
                resultado = "No Saludable. No es Solteroo"
            }
        }else {
            resultado = "No Saludable. Peso muy elevado"
        }
    }else {
        resultado = "No Saludable. Estatura no adecuada"
    }
    document.getElementById("resultadoAt").innerHTML = resultado;
}