//logical operators
console.log(true && true);
console.log(false && true);
console.log(true && false);

let haveJavaExperience = true;
let haveRubyExperience = false;
let canJion = haveJavaExperience && haveRubyExperience;
console.log('Approved',canJion);

let canJion1 = haveJavaExperience || haveRubyExperience;
console.log('Approved',canJion1);

console.log(true ||true);
console.log(true ||false);
console.log(false||false);
console.log('Refused',!canJion);