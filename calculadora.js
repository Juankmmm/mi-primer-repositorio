const promt = require("prompt-sync")();
console.log("=============");
console.log("Mi Calculadora");
console.log("================");
console.log("1: Sumar");
console.log("2: Restar");
console.log("3: Multiplicar");
console.log("4: Dividir");
console.log("==============");
let opcion = promt("Selecciona una opcion (1-4): ");
let num1 = Number(promt("Ingrese el primer numero: "));
let num2 = Number(promt("Ingrese el segundo numero: "));
if (opcion == "1"){
    console.log("El resultado de la suma es:", num1 + num2);
} else if (opcion == "2"){
    console.log("El resultado de la resta es:", num1 - num2);
} else if (opcion == "3"){
    console.log("El resultado de la multiplicacion es:", num1 * num2);
} else if (opcion == "4"){
    if (num2 === 0) { console.log("Error: No se puede dividir entre cero."); }
    else { console.log("El resultado de la division es:", num1 / num2); }
} else { console.log("Opcion no valida, intentalo de nuevo."); }
console.log("===========");



    