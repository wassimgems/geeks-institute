

/* exercice 1 */

const people = ["Greg", "Mary", "Devon", "James"];
people.splice(0, 1);

people[2] = "jason"
people.push("wassim")
console.log(people.indexOf("Mary"));
const people2 = people.slice(1, 3)
console.log(people2)

console.log(people.indexOf("Foo"))
/* be cause Foo si not in array "people" */

 const last = people[people.length - 1]
 console.log(last)
//  index = lenght - 1

for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
}

for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
    if (people[i] === "Devon") {
        break;
    }
}
// exercice 2
const colors = ["red", "blue", "green", "yellow","blue"];
const suffixes = ["st", "nd", "rd", "th", "th"];

for ( let i = 0 ; i < colors.length ; i++ ){
    console.log(`My #${i + 1}${suffixes[i]} choice is ${colors[i]}`)
}

// exercice 3


