#!/usr/bin/node
const argv = process.argv;
const argvLen = argv.length;
if (argvLen === 2 || argvLen === 3) {
  console.log(0);
} else {
  const item = argv.slice(2);
  item.map(Number).sort();
  console.log(item[item.length - 2]);
}
