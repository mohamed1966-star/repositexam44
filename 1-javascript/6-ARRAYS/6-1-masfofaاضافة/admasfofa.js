// 1--Ajout d'un article
let alphabet = ['c','d'];
alphabet[2] = 'e';
console.log(alphabet);
console.log(alphabet.length);
alphabet.push('f','g');
console.log(alphabet);
alphabet.unshift('a','b');
console.log(alphabet);
alphabet.splice(2,0,'stop','run');
console.log(alphabet);

