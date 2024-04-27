#include <ai.h>


AI_SHADER_NODE_EXPORT_METHODS(SimpleColorShaderMethods);

enum SimpleColorShaderParams {
	p_inputColor
};


node_parameters {
	AiParameterRGB("inputColor", 0.18f, 0.18f, 0.18f); // Default color is white
}


node_initialize {
	// Initialization code goes here
}


node_update {
	// Update code goes here
}


shader_evaluate {
	// Retrieve the input color parameter
	AtRGB inputColor = AiShaderEvalParamRGB(p_inputColor);

	// Set the output color parameter to the input color
	sg->out.RGB() = inputColor * 2.0f;
}


node_finish {
	// Cleanup code goes here
}


node_loader {
	if (i > 0) return false;
	node->methods = SimpleColorShaderMethods;
	node->output_type = AI_TYPE_RGB;
	node->name = "simple_color_shader";
	node->node_type = AI_NODE_SHADER;
	strcpy_s(node->version, AI_VERSION);
	return true;
}
