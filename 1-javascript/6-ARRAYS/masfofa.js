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

console.log('------------------------------------------');
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

console.log('-------------------------------------------');

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
console.log('-------------------------------------------------');

// 4--contraire du tableau MASFOFA
let numbers1 = [1,2,3,4,5];
function reverse(arr){
    let temp = [];
    for(let i in arr)
        temp.unshift(arr[i]);
    return temp;    
}
console.log(reverse(numbers1));
console.log('-------------------------------------------------');

// 5--التوابع في المصفوفات
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


// 6-7-Arrow function  الدوال السهمية والعبور على عناصر المصفوفة
let log = function(msg){
    console.log(msg);
}
log("Helllllooo");
console.log('----------------------------------------');
// param => {}
let log1 = msg => console.log(msg);
log('Hellllllllllllllllllo');
console.log('----------------------------------------');
//
let numbers3 =[5,12,8,130,44];
let result2 = numbers3.find(number => number > 10);
console.log(result2);
console.log('----------------------------------------');

// 8-ترتيب عناصر المصفوفات
const numbers4 = [4,1,3,2];
numbers4.sort();
console.log(numbers4);
//
const numbers5 = [4,3,2,1,18,12];
numbers5.sort((a,b) => {
    return a-b;
});
console.log(numbers5);

// الكائنات
// 1-2-الكائنات
let student = {
    name : 'Ahmad',
    age : 12,
    level : 6
};
console.log(student);
console.log(student.name);
console.log(student['name']+'  '+student['age']);
console.log('-----------------------------------------');

// 3-التوابع في الكائنات
let student1 = {
    name: 'jamal',
    age : 50,
    level :2,
    hello : function(){
        console.log('HELLO');
        
    }
}
student1.hello();
console.log('---------------------------------------------');

let student2 = {
    name: 'jamal',
    age : 50,
    level :2,
    hello : function(){
        //console.log('HELLO');
        console.log(this.name+' '+this.age+' '+this.level);
    }
}
student1.hello();
console.log('---------------------------------------------');
//
let student3 = {
    name: 'jigi',
    age : 80,
    level :1,
    hello : function(){
        console.log(this.name+' '+this.age+' '+this.level);
    },
    pass:function(){
        this.age++;
        this.level++;
    }
}
student3.hello();
student3.pass();
student3.hello();

console.log('---------------------------------------------');

// 4-التابع الباني on utilise le mot 'this' et 'new'

function Student(name,age,level){
    this.name = name;
    this.age = age;
    this.level;
    this.hello = function(){
        console.log(this.name+' '+this.age);
    }
    this.pass=function(){
        this.age++;
        this.level++;
    }
}
let student6=new Student('Toti',17,5);
student6.hello();
let student7=new Student('Jamal',15,8);
student7.hello();

// ادواة عامة
// 1-date كائن التاريخ
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
console.log(dob.getTime());
console.log('---------------------------------------------');
// UNIX TIMETAMP

console.log(dob.getTime());

if( dob.getTime()=== dob2.getTime()){
    console.log('Equal');
} else {
    console.log('Not Equal');
}
console.log('---------------------------------------------');

// 2-Regular Expression التعابير النظامية
const msg = 'Hello there ! My name is Hassan and my age is 20';
const regex = /name/;
const isMatched = regex.test(msg);
console.log(isMatched);

//التعامل مع الاخطاء
// 3- العبارة try catch
function sum(num1,num2){
    if(typeof num1!=='number') throw new Error('the first parameter must be a number at sum.');
    if(typeof num2!=='number') throw new Error('the second parameter must be a number at sum.');
    return num1 + num2;
}
try{
    console.log(sum(6,5));
} catch(error){
    console.log('O/ops! There is an error', error);
}