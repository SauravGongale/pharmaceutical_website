const mongoose=require("mongoose");

const contactSchema=new mongoose.Schema({
	fullname:{
		type:String,
		required:true
	},
	mobile:{
		type:Number,
		required:true
	},
	state:{
		type:String,
		required:true
	},
	subject:{
		type:String,
		required:true
	}
	
})

const contactReq = new mongoose.model("contactReq",contactSchema);

module.exports=contactReq;