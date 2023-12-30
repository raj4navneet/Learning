class Button 
{
  float x;
  float y;
  float w;
  float h;
  color col;
  color col2;
  boolean on;


Button(float tempX, float tempY, float tempW, float tempH) 
{
  x = tempX;
  y = tempY;
  w = tempW;
  h = tempH;
  col = color(random(0, 255), random(0, 255), random(0, 255));
  col2 = color(random(0, 255), random(0, 255), random(0, 255));
  on = false;
  
  if (mouseX > x && mouseX < x + w  && mouseY > y && mouseY < y + h) 
  {
  on = !on;
  }
  
}

  void rollover() 
  {
    if (mouseX > x && mouseX < x + w  && mouseY > y && mouseY < y + h) 
    {
      on = !on;
    }

  }

  void display()
  {
    if (on)
    {
      fill(col+col2);
    }
    else
    {
      fill(col);
    }
    stroke(0);
    rect(x, y, w, h);
  }
  
}
