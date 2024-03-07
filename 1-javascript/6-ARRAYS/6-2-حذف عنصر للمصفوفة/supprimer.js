// 2--Supprimer un article
let numbers = [1,2,3,4,5];
const last = numbers.pop();//supprimer le dernier
console.log(last);
console.log(numbers);

const first = numbers.shift();//supprimer le premier
console.log(first);
console.log(numbers);

const middle = numbers.splice(1,1);//supprimer ceux du milieu
console.log(middle);
console.log(numbers)

const middle1 = numbers.splice(1,2);
console.log(middle);
console.log(numbers);


