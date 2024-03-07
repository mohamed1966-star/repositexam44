//5-tawabia masfofa
let numbers2 = [5,12,8,130,44];
console.log(numbers2.includes(10));//غير موجود
console.log(numbers2.includes(12));//موجود
console.log(numbers2.indexOf(10));//-1 غير موجود
console.log(numbers2.indexOf(12));//1  موجود

let result = numbers2.find(function(number){
    return number > 10;
});
console.log(result);

let result1 = numbers2.filter(function(number){
    return number > 10;
});
console.log(result1);

let index = numbers2.findIndex(function(number){
    return number > 10;
});
console.log(index);
