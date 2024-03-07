// 3 concatenation
let greeting = 5+5;
console.log(greeting);
let greeting1 = '5'+'   5';
console.log(greeting1);
let name = 'hassan';
console.log('hello '+name);
//4 assignement operator
let x=8;
x+=2;
console.log(x);
x-=2;
console.log(x);
x*=2;
console.log(x);
x/=2;
console.log(x); 
//comparaison
let age=12;
console.log('Equal',age===12);
console.log('Not equal',age!==12);
console.log('larger',age > 12);
console.log('larger or Equal',age>=12);
console.log('less',age < 12);
console.log('less or Equal',age<=12);
//Equality operator
console.log(true && true);
console.log(false && true);
//Equality operator
console.log(1===1);
console.log(1==1);
console.log(1==='1');
console.log(1=='1');
console.log(true==1);
//exemple
let haveJavaExperience = true;
let haveRubyExperience = false;
let canjion = haveJavaExperience && haveRubyExperience;
console.log('Approved',canjion);

console.log(true ||true);
console.log(true ||false);
console.log(false||false);
console.log('Refused',!canjion);
//Bitwise operators
console.log(1&2);
console.log(1&3);
console.log(1|2);
//Read write Execution
// 00000100= 4 READ
// 00000010= 2 WRITE
const read = 4;
const write = 2;
const exe = 1;
let userPermission=read | write;
console.log(userPermission & read);
console.log(userPermission & exe);

