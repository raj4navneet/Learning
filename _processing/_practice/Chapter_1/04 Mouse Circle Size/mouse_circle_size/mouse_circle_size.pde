int circleSize = 0;
int circleX = 100;
int circleY = 100;
void setup() {
 size(1000, 1000);
}
void draw() 
{
 background(0);
 stroke(255);
 fill(175);
 float defaultSize = 20;
 float mouseSpeed = abs(mouseX - pmouseX) + defaultSize;
 //strokeWeight(mouseSpeed/4);
 ellipse(pmouseX, pmouseY, mouseSpeed, mouseSpeed);
}
