#!/usr/bin/node
const argv = process.argv.length;
const argv_len = argv.length;
if (argv_len === 2 || argv_len === 3)
{
	console.log(0);
}
else
{
	let item = argv.slice(2).sort();
	console.log(item[item.length - 2]);
}
