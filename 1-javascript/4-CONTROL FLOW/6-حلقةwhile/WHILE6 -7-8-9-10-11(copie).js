//Example while
let m =1;
while(m <= 10){
    console.log(m);
    m++;
}
console.log('----------------------------------')

//example
let number1 = 4;
let j = 1;
while (j <= 10) {
    console.log(j * number1);
    j++;
}

console.log('---------------------------------------------------')
// do while
let i = 1;
do {
    if (i % 2 === 0) console.log(i);
    i++;
} while (i <= 10);

console.log('---------------------------------------------------')
// مصفوفات FOR
const names = ['Ahmed', 'Ibrahim', 'AbdAllah', 'Omar'];

for (let i = 0; i < names.length; i++) {
    console.log(i, names[i]);
}

console.log('---------------------------------------------------')
// صفوفات WHILE
let x = 0;
while (x <  names.length ){
    console.log(x,names[x]);
    x++;
}

console.log('---------------------------------------------------')
// contraire
for(let i = names.length -1;i>=0; i--){
    console.log(i,names[i]);
}

console.log('---------------------------------------------------')
let x1 = names.length -1;
while (x1 >= 0 ){
   console.log(x1,names[x1]);
    x1--;
}

console.log('---------------------------------------------------')
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

console.log('---------------------------------------------------')
//for..of
for(let value of numbers){
    console.log(value);
}
//
let i1 = 0;
while( i1 < 10){
    i1++;
    console.log(i1);
}
//break..continue
let i2 = 0;
while( i2 < 10){
    i2++;
    if ( i2 === 3) continue;
    console.log(i2);
}

//
let i3 = 0;
while( i3 < 10){
    i3++;
    if ( i3 % 2 !== 0) continue;
    console.log(i3);
}
// 12 exercice
let cart = [10,25,15,20];
let total = 0;
for( let item of cart ) {
    total = total + item 
}
console.log(total);
// 13 exercice
const data = [5,true,'Hello',false,'Word',2];

for(let i4 = 0;i4 < data.length; i4++){
    console.log(data[i4]);
}

console.log('---------------------------------------------------')
//
for(let i5 = 0;i5 < data.length; i5++){
    if(typeof data[i5] === 'string') console.log(data[i5]);
}

console.log('---------------------------------------------------')
// exercice
let rows = prompt('Please enter rows count');
for (let row = 1;row <= rows;rows++){
    console.log('*');
}    
