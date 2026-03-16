#!/usr/bin/node
const argv_array = process.argv;
if(argv_array[2] === undefined)
{
	console.log("No argument");
}
else
{
	console.log(argv_array[2]);
}
