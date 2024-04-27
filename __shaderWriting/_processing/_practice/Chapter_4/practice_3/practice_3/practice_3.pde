float canvSizeX = 800;
float canvSizeY = 800;
float originX = canvSizeX*0.5;
float originY = canvSizeY*0.5;
float destinX = 0;
float destinY = 0;
float colFill = 255;

void setup()
{
 size(800,800);
 background(255);
}
void draw()
{
  
  fill(colFill*0.5);
  strokeWeight(3);
  rectMode(CENTER);
  rect(originX, originY, canvSizeX*0.9, canvSizeY*0.9); 
  fill(colFill);
  ellipse(originX, originY, canvSizeX*0.5, canvSizeY*0.5);
}
