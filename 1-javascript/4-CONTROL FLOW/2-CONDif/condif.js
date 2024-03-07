if(1===1){
    // Statement
    console.log('1 is equal to 1');
}
//let age=16;
let age=prompt('Enter age :');
if(age > 14){
    console.log('Age is above 14');
}else{
    if(age>10){
        console.log('Age is above 10');
    }else{
        console.log('Age is under or equal to 10');
    }
}

//let mark = 90;
let mark = prompt('Enter mark :');
let repeat = 1;
if (mark >= 80)
    console.log('Verry good');
else if(mark >= 60)
    console.log('Good');
else if(mark >= 50)
    console.log('Acceptable');
else{
    console.log('Failed');
    if(repeat > 0) console.log("Sorry you can't repeat.")
}
// you can write like this
let mark0 = prompt('Enter mark :');
let repeat0 = 1;
if (mark0 >= 80)
    console.log('Verry good');
if(mark0 >= 60 && mark0 < 80)
    console.log('Good');
if(mark0 >= 50 && mark0 < 60)
    console.log('Acceptable');
if(mark0<50){
    console.log('Failed');
    if(repeat0 > 0) console.log("Sorry you can't repeat.");
};
console.log('--------------------------------------');


