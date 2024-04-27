void setup()
{
  size(800, 800);
}

void draw()
{
  background(255);
  
  //GRID
  stroke(0);
  line (width/2, height/height, width/2 , height);
  line (width/width, height/2, width , height/2);
  
  //BOX
  noStroke();
  fill(50);
  rectMode(CENTER);
  
  if (mouseX < width/2 && mouseY < height/2)
  {
  rect(width*0.25,  height*0.25 ,width/2 , height/2);
  }
  else if (mouseX > width/2 && mouseY < height/2)
  {
  rect(width*0.75,  height*0.25 ,width/2 , height/2);
  }
  else if (mouseX < width/2 && mouseY > height/2)
  {
  rect(width*0.25,  height*0.75 ,width/2 , height/2);
  }
  else if (mouseX > width/2 && mouseY > height/2)
  {
  rect(width*0.75,  height*0.75 ,width/2 , height/2);
  }
}
