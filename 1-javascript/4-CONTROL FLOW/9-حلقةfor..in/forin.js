// for...in
const numbers = [10,4,30,12,68];

for(let index in numbers){
    console.log(index);
}

console.log('---------------------------------------------------')
//
for(let index in numbers){
    console.log(numbers[index]);
}

console.log('---------------------------------------------------')
//
for(let index in numbers){
    console.log(index,numbers[index]);
}