#include "ofMain.h"
#include "ofApp.h"

//========================================================================
int main( ){


	//Use ofGLFWWindowSettings for more options like multi-monitor fullscreen
	ofGLWindowSettings glSettings;
	glSettings.setSize(1024, 768);
	glSettings.windowMode = OF_WINDOW; //can also be OF_FULLSCREEN
	
	glSettings.setGLVersion(4, 1);

	auto window = ofCreateWindow(glSettings);

	ofRunApp(window, make_shared<ofApp>());
	ofRunMainLoop();

}
