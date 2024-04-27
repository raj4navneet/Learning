void setup()
{
  size(800, 800);
}

void draw() 
{
background(0);

for (int i = 0; i <width; i++)
{
noStroke();
fill(random(0, 255));
rect(i, 0, 10, height);
}
}
