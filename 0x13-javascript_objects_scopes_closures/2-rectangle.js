#!/usr/bin/node

module.exports = class Rectangle {
    constructor (w, h) {
      if ((w <= 0) || (h <= 0)) {
        let empty_obj = new Object();
      }
      else {
        this.width = w;
        this.height = h;
      }
    }
  };