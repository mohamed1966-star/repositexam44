// 4-Atabia Albani, On utilise le mot 'this' et 'new'

function Student(name,age,level){
    this.name = name;
    this.age = age;
    this.level=level;
    this.hello = function(){
        console.log(this.name+' '+this.age+' '+this.level);
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


