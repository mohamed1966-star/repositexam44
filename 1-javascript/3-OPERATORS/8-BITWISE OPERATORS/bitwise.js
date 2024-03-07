//Bitwise operators
console.log(1&2);
console.log(1&3);
console.log(1|2);

//Read write Execution
// 00000100= 4 READ
// 00000010= 2 WRITE
// 00000001= 1 EXECUTION
const read = 4;
const write = 2;
const exe = 1;
let userPermission=read | write;

console.log(userPermission & read);
console.log(userPermission & exe);