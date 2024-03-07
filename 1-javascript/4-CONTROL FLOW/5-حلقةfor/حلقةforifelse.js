let mark = 40;
if(mark >= 80){
    console.log('Very Good');
} else if(mark >= 60){
    console.log('Good');
} else if(mark >= 50){
    console.log('Acceptable');
} else {
    console.log('failed');
}
console.log('----------------------------------')
// supprimer les accolades et ajouter d'autres conditions
let mark1 = 40;
let repeat = 1;
if(mark1 >= 80)
    console.log('Very Good');
 else if(mark1 >= 60)
    console.log('Good');
else if(mark1 >= 50)
    console.log('Acceptable');
else {
    console.log('failed');
    if(repeat > 0) console.log('Sorry you can\'t repeat');
}
console.log('----------------------------------')
// Ternary Operator exemple1
let mark2 = 6;
let result = mark2 > 50 ? 'Passed':'Failed';
console.log(result);
console.log('----------------------------------')
//exemple2
let age = 15;
let status = age >= 16 ? 'Accepted':'Decliend';
console.log(status);
console.log('----------------------------------')
//exemple3
let age1 = 15;
let mark3 = 40
let status1 = age1 >= 16 ?(mark3 >= 50 ? 'Accepted': 'Failed') : 'Decliend';
console.log(status1);
console.log('----------------------------------')
//Switch
let day = 11;
switch(day){
    case 0:
        console.log('Sunday');
    break;
    case 1:
        console.log('Monday');
    break;
    case 2:
        console.log('Thuesday');
    break;
    case 3:
        console.log('Wednesday');
    break;
    case 4:
        console.log('Thursday');
    break;
    case 5:
        console.log('Friday');
    break;
    case 6:
        console.log('Saturday');
    break;
    default:
        console.log('Invalid day');
    break;
}
console.log('----------------------------------')
// meme travail avec if..else
if(day === 0) console.log('Sunday');
else if(day === 1) console.log('Monday');
else if(day === 2) console.log('Thuesday');
else if(day === 3) console.log('Wednesday');
else if(day === 4) console.log('Thursday');
else if(day === 5) console.log('Friday');
else if(day === 6) console.log('Saturday');
else console.log('Invalid day');
console.log('----------------------------------')
// FOR
for(let i = 0; i<3;i++){
    console.log('HIHI Hello');
    console.log('HIHI ');
}
console.log('----------------------------------')
//Example1
for(let i = 0;i<10;i++)
console.log(i);
console.log('----------------------------------')
//Example2
for(let i = 1; i<=10; i++)
    if(i % 2 == 0)console.log(i);
console.log('----------------------------------')
//Example4
for(let i = 10; i >= 1; i--)
    if(i % 2 == 0)console.log(i);
console.log('----------------------------------')
//Example5
let i = 0;
let number = 4;
for(i = 1; i <= 10; i++)
    console.log(number*i);
console.log('----------------------------------')
// Example6
for(let i = 0; i < 5; i++){
    for(let j = 1; j < 4; j++) console.log(j);
}
console.log('----------------------------------')
