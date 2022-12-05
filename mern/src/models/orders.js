const mongoose=require("mongoose");

const orderSchema=new mongoose.Schema({
	firstname:{
		type:String,
		required:true
	},
	lastname:{
		type:String,
		required:true
	},
	email:{
		type:String,
		required:true,
		unique:true
	},
	address:{
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
	pincode:{
		type:Number,
		required:true
	},
	paymentMethod:{
		type:String,
		required:true
	},
	cardName:{
		type:String,
		required:true
	},
	cardNum:{
		type:Number,
		required:true
	},
	validUpto:{
		type:Date,
		required:true
	},
	cvv:{
		type:Number,
		required:true
	},
})

const Order = new mongoose.model("Order",orderSchema);

module.exports=Order;
