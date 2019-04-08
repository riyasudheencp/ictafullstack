const express=require('express');
var app=express();
app.get('/',(req,res)=>{
    res.send("hello frinds");
});
app.get('/home',(req,res)=>{
    res.send("welcome");
});
app.get('/contact',(req,res)=>{
    res.send("my contact page");
});
app.get('/home/contact',(req,res)=>{
    res.send('[{"name":"riyas",age:23}{"name":"nikhil""age":25}]');
});

app.listen(5000);