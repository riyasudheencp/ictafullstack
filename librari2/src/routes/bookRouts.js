const express=require('express');
const booksRouter=express.Router();

function router(nav){
var books=[
    {
        title:"war and piese",
        genre:"historical fiction",
        autho:"riyas",
    },
    {
        title:"war",
        genre:"fiction",
        autho:"nikhil",
    },
    {
        title:"piese",
        genre:"historical",
        autho:"asil",
    }
];
booksRouter.route('/').get((req,res)=>{
    res.render
   ( "books",
    {
        nav, 
       
        title:"books",books
    }
);
   
});
booksRouter.route('/:id')
.get((req,res)=>{
    const id=req.params.id;
    res.render
    ( "book",
     {
         nav,
        
         title:"books",book:[id]
     }
 );
    
 });

return booksRouter;
}
module.exports=router;