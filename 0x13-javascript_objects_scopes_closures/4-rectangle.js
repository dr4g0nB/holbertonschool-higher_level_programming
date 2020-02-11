#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }

    Rectangle.prototype.print = function () {
      for (let alto = 0; alto < h; alto++) {
        let printRectangle = '';
        for (let ancho = 0; ancho < w; ancho++) {
          printRectangle += 'X';
        }
        console.log(printRectangle);
      }
    };

    Rectangle.prototype.rotate = function () {
      let swap = this.width;
      swap = this.height;
      this.height = this.width;
    }

    Rectangle.prototype.double = function () {
      this.width = this.width * 2;
      this.height = this.height * 2;
    }
  }
};
