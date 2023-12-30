// A polar coordinate
float r = 0;
float theta = 0;
int muliplier = 10;
void setup() {
size(800, 800);
background(255);
}
void draw() {
float x = r * cos(theta);
float y = r * sin(theta);
noStroke();
fill(0);
ellipse(x + width/2, y + height/2, 2* muliplier, 2* muliplier);
// Increment the angle
theta += 0.01 * muliplier;
r += 0.1 * muliplier; 
}
