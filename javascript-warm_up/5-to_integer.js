#!/usr/bin/node
const num = process.argv[2];
if (parseInt(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
