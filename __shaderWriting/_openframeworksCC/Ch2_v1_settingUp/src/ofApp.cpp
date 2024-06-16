#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){

	triangle.addVertex(glm::vec3(-1.0f, 1.0f, 0.0f));
	triangle.addVertex(glm::vec3(-1.0f, -1.0f, 0.0f));
	triangle.addVertex(glm::vec3(1.0f, -1.0f, 0.0f));

	triangle.addColor(ofFloatColor(1.0f, 0.0f, 0.0f, 1.0f));
	triangle.addColor(ofFloatColor(0.0f, 1.0f, 0.0f, 1.0f));
	triangle.addColor(ofFloatColor(0.0f, 0.0f, 1.0f, 1.0f));

	shader1.load("first_vertex.vert", "first_fragment.frag");

}

//--------------------------------------------------------------
void ofApp::update(){

}

//--------------------------------------------------------------
void ofApp::draw(){
	shader1.begin();
	triangle.draw();
	shader1.end();
}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){
	/*
	if (key == OF_KEY_UP) {
		glm::vec3 curPos = triangle.getVertex(2);
		triangle.setVertex(2, curPos + glm::vec3(0, -20, 0));
	}
	else if (key == OF_KEY_DOWN) {
		glm::vec3 curPos = triangle.getVertex(2);
		triangle.setVertex(2, curPos + glm::vec3(0, +20, 0));
	}
	*/

}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){

}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){

}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y){

}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){

}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){

}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){ 

}
