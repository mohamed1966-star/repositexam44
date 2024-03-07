function hello(name){
    console.log('Hello '+name);
}
hello('hassoub');
console.log('---------------------------------------------');
//
function sum(x,y){
    console.log(x+y);
}
sum(5,9);
//
function sum1(x,y){
    return x+y;
}
let result = sum1(2,4);
console.log(result);
console.log('---------------------------------------------');
//
function filterArray(array){
    for(let item of array){
        if(typeof item==='string')
        console.log(item);
    }
}
filterArray(['ibrahim',254,'totoch',59]);