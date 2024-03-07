// 3-tawabia fi alkainat
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
//
let student2 = {
    name: 'jamal',
    age : 50,
    level :2,
    hello2 : function(){
        //console.log('HELLO');
        console.log(this.name+' '+this.age+' '+this.level);
    }
}
student2.hello2();
console.log('---------------------------------------------');
//
let student3 = {
    name: 'jigi',
    age : 80,
    level :1,
    hello3 : function(){
        console.log(this.name+' '+this.age+' '+this.level);
    },
    pass:function(){
        this.age++;
        this.level++;
    }
}
student3.hello3();
student3.pass();
student3.hello3();

