float x = 0;
float speed = 6;
float randomSpeed = 1;
float colR = 30;
float colG = 80;
float colB = 110;


void setup() 
{
frameRate(60);
size(800, 800);
}


void draw() 
{
  
background(255);

x = x + speed;

if ((x > width) || (x < 0)) 
{
speed = speed * -1;
colR = random(30,180);
colG = random(30,180);
colB = random(30,180);
}

colR = colR + 1;
colG = colG + 1;
colB = colB + 1;
// Display circle at x location
stroke(0);
fill(colR , colG, colB);
ellipse(x, height/2, width/4, width/4);

}
