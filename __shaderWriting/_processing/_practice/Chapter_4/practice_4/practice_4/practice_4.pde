void setup() {
  size(800, 200);
}
void draw() {
  background(255);

  stroke(0);
  rectMode(CENTER);
  fill(255);
  rect(width/2, height/2, width*0.9, height*0.9);
  line(width*0, height*0, width, height);
  line(width, height*0, width*0, height);
  fill(150);
  ellipse(width*0.5, height*0.5, width*0.5, height*0.5);
  rect(width*0.85, height*0.5, width*0.1, height*0.1 );
  rect(width*0.15, height*0.5, width*0.1, height*0.1 );
  
}
