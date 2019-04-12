const mongoose=require('mongoose');
mongoose.connect('mongodb://localhost:27017/librari95');
const Schema=mongoose.Schema;
var NewBookSchema=new Schema({
    title:String,
    author:String,
    genre:String
});
var bookdata=mongoose.model('book-data',NewBookSchema);
module.exports=bookdata;