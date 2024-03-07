//break..continue
let i2 = 0;
while( i2 < 10){
    i2++;
    if ( i2 === 3) continue;
    console.log(i2);
}
console.log('-----------------------------------------')
//
let i3 = 0;
while( i3 < 10){
    i3++;
    if ( i3 % 2 !== 0) continue;
    console.log(i3);
}
console.log('-----------------------------------------')
let i4 = 0;
while( i4 < 10){
    i4++;
    if ( i4 === 3) break;
    console.log(i4);
}
console.log('-----------------------------------------')
let i5 = 0;
while( i5 < 10){
    i5++;
    if ( i5 % 2 !== 0) break;
    console.log(i5);
}
console.log('-----------------------------------------')
// 12 exercice
let cart = [10,25,15,20];
let total = 0;
for( let item of cart ) {
    console.log(item);
    total = total + item 
}
console.log(total);

console.log('-----------------------------------------')
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
/// exercice
let rows = prompt('Please enter rows count');
for (let row = 1;row <= rows;row++){
    stars='';
    for(i=0;i<row;i++){
        stars+='*';
    }
    console.log(stars);
}