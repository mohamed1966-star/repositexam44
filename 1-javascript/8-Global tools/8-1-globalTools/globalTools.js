// Global Tools
// 1-date
let myDate = new Date();
console.log(myDate);
console.log('-----------------------------------------');
//
let dob = new Date('1996-03-14 04:00:30');
let dob2 = new Date('2000-10-04 00:00:00');
console.log(dob);
console.log(dob.getFullYear());
console.log(dob.getMonth());
console.log(dob.getDate());
console.log(dob.getHours());
console.log('-----------------------------------------');
console.log(dob2);
console.log(dob2.getFullYear());
console.log(dob2.getMonth());
console.log(dob2.getDate());
console.log(dob2.getHours());
console.log(dob2.getTime());
console.log('---------------------------------------------');
// UNIX TIMETAMP

console.log(dob.getTime());

if( dob.getTime()=== dob2.getTime()){
    console.log('Equal');
} else {
    console.log('Not Equal');
}