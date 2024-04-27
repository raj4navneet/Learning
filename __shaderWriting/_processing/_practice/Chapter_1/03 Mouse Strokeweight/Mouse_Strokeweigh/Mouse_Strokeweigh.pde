void setup()
{
  size(1000,1000);
  
}

void draw()
{
  stroke (0);
  float mouseSpeed = abs(mouseX - pmouseX);
  strokeWeight(mouseSpeed/4);
  line(pmouseX, pmouseY, mouseX, mouseY);
}
  
