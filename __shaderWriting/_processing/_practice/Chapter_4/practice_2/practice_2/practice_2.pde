float canvSizeX = 800;
float canvSizeY = 800;
float originX = canvSizeX/2;
float originY = canvSizeY/2;
float destinX = 0;
float destinY = 0;
float colStroke = 0;

void setup()
{
 size(800,800);
}
void draw()
{
  stroke(colStroke);
  strokeWeight(10);
  line(originX, originY, canvSizeX*0.5, canvSizeY*0);
  line(originX, originY, canvSizeX*0, canvSizeY);
  line(originX, originY, canvSizeX, canvSizeY);
}
