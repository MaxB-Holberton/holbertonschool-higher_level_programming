#!/usr/bin/node
const argvArray = process.argv;
if (argvArray[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argvArray[2]);
}
