

void setup()
{
  frameRate(60);
  size(800, 800);
}

float posX = 400;
float posY = 200;
float speed = 10;
float gravity = 0.5;

void draw()
{
 background(150);
 noStroke();
 fill(50);
 
 int sizeW = width/8;
 int sizeH = height/8;
 
 ellipse(posX , posY, sizeW, sizeH);
  
 posY += speed; 
 speed += gravity;
 
 if (posY > height-(sizeH/2))
 {
   speed = speed * (-0.75);
   posY = height-(sizeH/2);
 }

 }
