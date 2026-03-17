#!/usr/bin/node
const argv = process.argv;
const argvLen = argv.length;
if (argvLen === 2 || argvLen === 3) {
  console.log(0);
} else {
  const item = argv.slice(2).map(Number);
  item.sort((a, b) => a - b);
  console.log(item[item.length - 2]);
}
