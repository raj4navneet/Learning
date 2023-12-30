void setup() 
{
size(800, 800);
}
void draw() 
{
background(255);
float spacing = 2;
for (int i = 0; i <= width; i+= spacing)
{
  float distance = abs(mouseX-i);
  rectMode(CENTER);
  fill(distance);
  noStroke();
  rect(i, height/2, spacing/2, height);
  println(i);
}
}
