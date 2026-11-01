

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


let  number = prompt("entre a number")
console.log(typeof number);
number = Number(number);

while (number < 10) {
    number = Number(prompt ("Enter number greater than 10"));
}
alert(" Good ");

// exercice 4

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

console.log(building.numberOfFloors)
console.log (building.numberOfAptByFloor.firstFloor)
console.log (building.numberOfAptByFloor.secondFloor)
console.log(building.nameOfTenants[1])

let sum = building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.dan[1]
if ( sum > building.numberOfRoomsAndRent.david[1] ){
    building.numberOfRoomsAndRent.dan[1] = 1200;
}

// exercice 5


const family = {
    parents: "Alice",
    children: "Charlie",
    lastName: "Smith",
};

for ( let key in family){
    console.log(key);
}
for (let key in family){
    console.log(family[key])
}

// exercice 6

const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'reindeer'
}

let sentence = '';
for (let keys in details) {
     sentence += keys + ' ' + details[keys] + ' ';
}
console.log(sentence);

// exercice 7

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

const sscret = names

.map(name => name[0])
.sort()
.join('');
console.log(sscret)