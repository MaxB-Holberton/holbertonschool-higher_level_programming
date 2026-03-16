#!/usr/bin/node
const num = process.argv[2];
if (parseInt(num))
{
	for (let i = 0; i < parseInt(num); i++)
	{
		let sq = "";
		for (let j = 0; j < parseInt(num); j++)
		{
			sq += "X";
		}
		console.log(sq);
	}
}
else
{
	console.log("Missing size");
}
