int fill0 = 0;
int fill1 = 0;
int fill2 = 0;
int fill3 = 0;

void setup()
{
  size(800, 800);
}

void draw()
{
  background(255);
  

  
  //BOX
  noStroke();
  rectMode(CENTER);
  

   if (mouseX < width/2 && mouseY < height/2)
  {
    fill0 = 45;
  }
  else if (mouseX > width/2 && mouseY < height/2)
  {
    fill1 = 45;
  }
  else if (mouseX < width/2 && mouseY > height/2)
  {
    fill2 = 45;
  }
  else if (mouseX > width/2 && mouseY > height/2)
  {
    fill3 = 45;
  }
  
  
  fill0 += 5;
  fill1 += 5;
  fill2 += 5;
  fill3 += 5;

  
  fill(fill0);
  rect(width*0.25,  height*0.25 ,width/2 , height/2);
  fill(fill1);
  rect(width*0.75,  height*0.25 ,width/2 , height/2);
  fill(fill2);
  rect(width*0.25,  height*0.75 ,width/2 , height/2);
  fill(fill3);
  rect(width*0.75,  height*0.75 ,width/2 , height/2);
  
  
  //GRID
  stroke(0);
  line (width/2, height/height, width/2 , height);
  line (width/width, height/2, width , height/2);
}
