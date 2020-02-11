#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
    /** else {
      const emptyObj = {};
    } */

    Rectangle.prototype.print = function () {
      for (let alto = 0; alto < h; alto++) {
        let printRectangle = '';
        for (let ancho = 0; ancho < w; ancho++) {
          printRectangle += 'X';
        }
        console.log(printRectangle);
      }
    };
  }
};
