//declaring xpos and ypos
int[] xpos = new int[300];
int[] ypos = new int[300];

void setup()
{
  frameRate(60);
  size(800, 800);

//Intialising xpos and ypos with intial value at 0
for (int i=0; i<xpos.length; i++)
 {
 xpos[i] = 0;
 ypos[i] = 0;
 }
}

void draw()
{
  
background(255);
// shifting array values
for(int i=0; i<xpos.length-1; i+=1)
{
  xpos[i] = xpos[i+1];
  ypos[i] = ypos[i+1];
}

// assigning xpos and ypos' last value to mouseX and mouseY  
 xpos[xpos.length-1] = mouseX;
 ypos[ypos.length-1] = mouseY;
 
for(int i=0; i< xpos.length; i+=1)
{
 noStroke();
 fill(constrain(255 -i*5, 0, 255));
 ellipse(xpos[i], ypos[i], i/4, i/4);
 println(xpos[i], ypos[i]);
}
}
