float circleX = 200;
float circleY = 200;
float circleW = 200;
float circleH = 200;
float circleStroke = 255;
float circleFill = 0;
float backgroundColor = 255;
float change = 3;

void setup()
{
 size(800,800);
}

void draw()
{
 background(backgroundColor);
 stroke(circleStroke);
 fill(circleFill);
 ellipse(circleX, circleY, circleW, circleH);
 ellipse(circleX*change, circleY, circleW, circleH);
 ellipse(circleX, circleY*change, circleW, circleH);
 ellipse(circleX*change, circleY*change, circleW, circleH);
 
}
