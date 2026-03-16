#!/usr/bin/node
function factorial(num)
{
	if (num > 1)
	{
		return(num * factorial(num - 1));
	}
	return (1);
}

const number = process.argv[2];
if (parseInt(number))
{
	console.log(factorial(parseInt(number)));
}
else
{
	console.log(1);
}
