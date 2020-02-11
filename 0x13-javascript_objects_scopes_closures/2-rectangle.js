#!/usr/bin/node

module.exports = class Rectangle {
<<<<<<< HEAD
  constructor (w, h) {
    if ((w <= 0) || (h <= 0)) {
      let empty_obj = new Object();
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
=======
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
>>>>>>> c4544a59fd5aec43ec3b8016b0b25e7bc499d4d7
