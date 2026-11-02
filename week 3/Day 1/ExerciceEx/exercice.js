
// exercice 1


displayNumbersDivisible(divisor);

function displayNumbersDivisible(){
    let i = 0;
    let sum = 0;
  while (i <= 500){
     if (i % divisor === 0){
         console.log("outcome :" + i);
         sum += i;
         
} i++
}
console.log("sum :" + sum);
}

