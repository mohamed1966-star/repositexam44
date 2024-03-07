function sum(x,y){
    console.log(arguments);
    return x+y
}
const result = sum(2,7,5);
console.log(result);
console.log('--il fait la somme des trois nombres-------------------------------------');
//
function sum(x,y){
    let total = 0;
    for(let num of arguments)
    total+=num;
    return total;
}
const result1 = sum(2,7,5,10);
console.log(result1);
console.log('----la somme de tous les nombres-----------------------------------');