const mongoose=require("mongoose");

const PackageSchema=new mongoose.Schema({
	firstname:{
		type:String,
		required:true
	},
	lastname:{
		type:String,
		required:true
	},
	packages:{
		type:String,
		required:true
	},
	plan:{
		type:String,
		required:true
	},

	email:{
		type:String,
		required:true,
		unique:true
	},
	mobile:{
		type:Number,
		required:true
	},
	city:{
		type:String,
		required:true
	},
})

const packBooking = new mongoose.model("packBooking",PackageSchema);

module.exports=packBooking;