var num1=120;
var num2=160;
var rev=0;
var rem=0;
var num3=add(num1,num2);
var num4=sub(num1,num2);
var num5=reverse(num1);

console.log(num4);
console.log(num3);
console.log(rev);
function add(x,y)

{
    z=x+y;
    return z;
}
function sub(x,y)

{
    a=x-y;
    return a;
}
function reverse(a){
    while(a>0) {
    rem=a%10;
    rev=rev*10+rem;
    a=parseInt(a/10);

}
return rev;
}