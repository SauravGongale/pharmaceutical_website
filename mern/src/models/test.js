const mongoose=require("mongoose");

const testSchema=new mongoose.Schema({
	name:{
		type:String,
		required:true
	},
	Blood:{
		type:String,
		required:true
	},
	Tests:{
		type:String,
		required:true
	},
	slot:{
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

const testBooking = new mongoose.model("testBooking",testSchema);

module.exports=testBooking;