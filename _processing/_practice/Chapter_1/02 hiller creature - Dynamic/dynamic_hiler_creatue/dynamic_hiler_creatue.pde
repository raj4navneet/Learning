void setup()
{
size(1000, 1000);
frameRate(60);
}
void draw()
{
  
background(150);

//body
fill(0);
rectMode(CENTER);
rect(mouseX, mouseY, 380, 200);

//ears
fill (20,110,65);
strokeWeight(20);
ellipse(mouseX-150, mouseY-250, 100, 150);
ellipse(mouseX+150, mouseY-250, 100, 150);

//Arms and legs
strokeWeight(50);
line(mouseX-300, mouseY-75, pmouseX+300, pmouseY-75);
line(mouseX-100, mouseY, pmouseX-100, pmouseY+200);
line(mouseX+100, mouseY, pmouseX+100, pmouseY+200);

//head
strokeWeight(10);
rectMode(CENTER);
rect(mouseX, mouseY-200, 300, 500);

//eye
colorMode(HSB, 100);
fill(0, mouseY/10 , mouseY/10);
ellipse(mouseX, mouseY-250, 175, 75);

colorMode(RGB, 255);
//hat
fill(0);
ellipse(mouseX, mouseY-450, 400, 150);

//eyebrow
strokeWeight(35);
point(mouseX,mouseY-250);
line(mouseX-100, mouseY-300, mouseX+100,  mouseY-300);

//goatee
rectMode(CENTER);
rect( mouseX,  mouseY+25, 50, 75);

//mouth
stroke(0);
strokeWeight(45);
line( mouseX-50,  mouseY-100,  mouseX+50,  mouseY-100);
}
void mousePressed() 
{
translate(0, -20);
line(mouseX-100, mouseY-300, mouseX+100,  mouseY-300);

}
