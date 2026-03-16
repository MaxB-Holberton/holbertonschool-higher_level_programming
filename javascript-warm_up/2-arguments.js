#!/usr/bin/node
const argv_len = process.argv.length;
if (argv_len == 2)
{
	console.log("No argument");
}
else if (argv_len == 3)
{
	console.log("Argument found");
}
else
{
	console.log("Arguments found");
}
