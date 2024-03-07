function sum(x,y){
    if(y===undefined)y=1;
    return x+y
}
const result = sum(2);
console.log(result);
console.log('---------------------------------------');
//
function sum1(x,y=4){
    return x+y
}
const result1 = sum1(2);
console.log(result1);