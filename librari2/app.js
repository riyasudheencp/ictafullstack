const express=require('express');
const chalk=require('chalk')
const path=require('path')


const authorsRouter=express.Router();
var app=express();

app.set('views','./src/views');
app.set('view engine','ejs');
app.use(express.static(path.join(__dirname,"/public")))


app.use('/authors',authorsRouter);
const nav =[
    {link:'/books',title:'books'},
    {link:'/authors',title:'authors'},
    {link:'/addbook',title:'Admin'}
    
   ];
   const booksRouter=require('./src/routes/bookRouts')(nav);
   const adminRouter=require('./src/routes/adminroutes')(nav);
   app.use('/books',booksRouter);
   app.use('/addbook',adminRouter);
app.get('/',(req,res)=>{
 res.render('index',{
    nav,
     title:"librari"});

});

authorsRouter.route('/').get((req,res)=>{
    res.render(
        "authors",{
       title:"authors"
    });
   
});


app.listen(3000,function(){
console.log('listening to port'+chalk.green('3000'));
});