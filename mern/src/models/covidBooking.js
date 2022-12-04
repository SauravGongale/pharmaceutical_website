const mongoose=require("mongoose");

const bookingSchema=new mongoose.Schema({
	firstname:{
		type:String,
		required:true
	},
	lastname:{
		type:String,
		required:true
	},
	gender:{
		type:String,
		required:true
	},
	email:{
		type:String,
		required:true,
		unique:true
	},
	mobile:{
		type:String,
		required:true
	},
	city:{
		type:String,
		required:true
	},
})

const covidBooking = new mongoose.model("covidBooking",bookingSchema);

module.exports=covidBooking;