#!/usr/bin/node

const arg = parseInt(process.argv[2]);
function factorialofarg (arg) {
    if (!(arg)) {
        return 1;
    }
    arg *= factorialofarg(arg - 1);
    return arg;
}

console.log(factorialofarg(arg));