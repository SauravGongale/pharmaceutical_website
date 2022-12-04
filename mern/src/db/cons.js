const mongoose = require("mongoose");

mongoose.connect("mongodb+srv://Pharma:pharma@cluster0.a2f2ko5.mongodb.net/test",(err)=>{
	if(!err){
		console.log("---Database Connected-----");
	}else{
		console.log("Connection Error");
	}
})