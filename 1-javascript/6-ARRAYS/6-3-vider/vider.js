// 3--vider almsfofa
let langs = ['JS','PHP','C++'];
langs = [];
console.log(langs);
//
let langs1 = ['JS','PHP','C++'];
let clone = langs1;
langs1 = [];
console.log(langs1);
console.log(clone);
console.log('-------------------------------------------------');

let clone1 = langs1;
langs1.length = 0;
console.log(langs1);
console.log(clone1);

