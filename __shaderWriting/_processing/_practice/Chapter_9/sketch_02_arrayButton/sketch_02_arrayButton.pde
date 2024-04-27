Button[] buttons = new Button[30];

void setup() 
{
  frameRate(25);
  size(800, 800);
  for (int i = 0; i < buttons.length; i++) 
  {
    buttons[i] = new Button(random(0, 600), random(0, 600), random(0, 200), random(0, 200)) ;
  }
}

void draw() 
{
  background(100);
  
  for (int i = 0; i < buttons.length; i++) 
  {
    buttons[i].display();
  }
}

void mousePressed() 
{
  for (int i = 0; i < buttons.length; i++) 
  {
    buttons[i].rollover();
  }
}
