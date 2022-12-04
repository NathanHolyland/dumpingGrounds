class Vector {
    constructor(x, y) {
      this.x = x;
      this.y = y;
    }
    magnitude() {
      return (this.x**2 + this.y**2)**1/2;
    }
    add(vec) {
      return new Vector(this.x+vec.x, this.y+vec.y);
    }
    sub(vec) {
      return new Vector(this.x-vec.x, this.y-vec.y);
    }
    
  }
  
  x = new Vector(10, 2);
  y = new Vector(2, 3);
  console.log(x.add(y))