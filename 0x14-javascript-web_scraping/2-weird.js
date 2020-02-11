#!/usr/bin/node

const request = require('request');

const getRequest = request.get(process.argv[2], )
/** const getRequest = request.get(process.argv[2]);*/
console.log("code: ", getRequest);
