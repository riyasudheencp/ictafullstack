const mymodule=require('./addmodule');
var x=45;
var y=46;
var z=mymodule.addnum(x,y);
var a=mymodule.subnum(x,y);
var b=mymodule.mulnum(x,y);
var c=mymodule.divnum(x,y);
console.log(z);
console.log(a);
console.log(b);
console.log(c);