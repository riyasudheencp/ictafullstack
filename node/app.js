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
    res.send("my contact page");
});

app.listen(5000);