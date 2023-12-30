int x = 400;
int y = 400;
int w = 400;
int h = 400;
float r;
float g;
float b;
void setup() {
 size(800, 800);
 frameRate(10);
}
void draw() 
{
 background(255);
 stroke(0);
if (mouseX >= x-w/2 && mouseX<= x+w/2 && mouseY >= y-h/2 && mouseY<= y+h/2)
{
   r = random(255);
   g = random(255);
   b = random(255);
   fill(r,g,b);  
}
else
{
   fill(255,255,225);
}
rectMode(CENTER);
 rect(x, y, w, h);
}
