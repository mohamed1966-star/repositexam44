function sum(...args){
    console.log(args);
}
const result1 = sum(2,3,5,10,40);
console.log(result1);
console.log('---------------------------------------');
//
function sum(...args){
    let total = 0;
    for(let num of args)
    total+=num;
    return total;
}
const result2 = sum(2,3,5,10,40);
console.log(result1);
console.log('---------------------------------------');
//
function sum(multiply,...args){
    let total = 0;
    for(let num of args)
    total+=num;
    return multiply * total;
}
const result3 = sum(2,2,3,5,10,40);
console.log(result3);
