//VARIABLES
int posX = 0;
int posY = 0;
int scaleW = width;
int scaleH = height;
int speed  = 50;

void setup()
{
  size(800, 800);
  frameRate(60);
}

void draw()
{
  
  background(150);
  fill(50);
  noStroke();
  rect(posX, posY, scaleW, scaleH);
  
  //Left to Right
  if (posY == 0 && posX >= 0 && posX < width-scaleW)
  {
    println(posX, posY, scaleW, scaleH);
    posX += speed;
  }
  //Up to Down
  else if (posX == width-scaleW && posY >= 0 && posY < height-scaleH)
  {
    println(posX, posY, scaleW, scaleH);
    posY += speed;
  }
  //Right to Left
  else  if (posY == height-scaleH && posX <= width-scaleW && posX > 0)
  {
    println(posX, posY, scaleW, scaleH);
    posX -= speed;
  }
  //Down to Up;
  else if (posX == 0 && posY <= height-scaleH && posY > 0)
  {
    println(posX, posY, scaleW, scaleH);
    posY -= speed;
  }
  else
  {
    println(posX, posY, scaleW, scaleH);
    rect(posX, posY, width/4, height/4);
  }
}
