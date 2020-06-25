"use strict"

const mat4 = glMatrix.mat4;

// Vertex shader
const vertexSource = `

attribute vec4 aVertexPosition;

uniform mat4 uModelViewMatrix;
uniform mat4 uProjectionMatrix;
uniform float time;

varying lowp vec4 position;

void main()
{
//	gl_Position = uProjectionMatrix * uModelViewMatrix * aVertexPosition;
	gl_Position = aVertexPosition;
	position = aVertexPosition;
}
`;

const fragmentSource = `

precision highp float;

uniform float time;
varying lowp vec4 position;

void main()
{
	float a = sin(time);
	gl_FragColor = vec4(position.xy, a, 1.0);
}
`;

function initShaderProgram(gl, vsSource, fsSource) {
	const vertexShader = loadShader(gl, gl.VERTEX_SHADER, vsSource);
	const fragmentShader = loadShader(gl, gl.FRAGMENT_SHADER, fsSource);

	// Create the shader program
	const shaderProgram = gl.createProgram();
	gl.attachShader(shaderProgram, vertexShader);
	gl.attachShader(shaderProgram, fragmentShader);
	gl.linkProgram(shaderProgram);

	// If creating the shader program failed, alert
	if (!gl.getProgramParameter(shaderProgram, gl.LINK_STATUS)) {
		alert('Unable to initialize the shader program: ' + gl.getProgramInfoLog(shaderProgram));
		return null;
	}
	return shaderProgram;
}

function loadShader(gl, type, source) {
	const shader = gl.createShader(type);
	gl.shaderSource(shader, source);
	gl.compileShader(shader);

	if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
		alert('An error occurred compiling the shaders: ' + gl.getShaderInfoLog(shader));
		gl.deleteShader(shader);
		return null;
	}
	return shader;
}

function initBuffers(gl) {
	const positionBuffer = gl.createBuffer();
	gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
	const positions = [
		-1.0,  1.0,
		1.0,  1.0,
		-1.0, -1.0,
		1.0, -1.0,
	];
	gl.bufferData(gl.ARRAY_BUFFER,
		new Float32Array(positions),
		gl.STATIC_DRAW);

	return {
		position: positionBuffer,
	};
}

function drawScene(gl, programInfo, buffers, time, dimensions) {
	gl.viewport(0,0,dimensions[0], dimensions[1]);
	gl.clearColor(0.5, 0.5, 0.5, 1.0);
	gl.clearDepth(1.0);
	gl.enable(gl.DEPTH_TEST);
	gl.depthFunc(gl.LEQUAL);
	gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

	const fieldOfView = 45 * Math.PI / 180;
	const aspect = dimensions[0] / dimensions[1];
	const zNear = 0.1;
	const zFar = 100.0;
	const projectionMatrix = mat4.create();
	mat4.perspective(projectionMatrix, fieldOfView, aspect, zNear, zFar);
	const modelViewMatrix = mat4.create();
	mat4.translate(modelViewMatrix, modelViewMatrix, [-0.0, 0.0, -6.0]);
	{
		const numComponents = 2;
		const type = gl.FLOAT;
		const normalize = false;
		const stride = 0;
		const offset = 0;
		gl.bindBuffer(gl.ARRAY_BUFFER, buffers.position);
		gl.vertexAttribPointer(programInfo.attribLocations.vertexPosition, numComponents, type, normalize, stride, offset);
		gl.enableVertexAttribArray(programInfo.attribLocations.vertexPosition);
	}
	gl.useProgram(programInfo.program);
	gl.uniformMatrix4fv(programInfo.uniformLocations.projectionMatrix, false, projectionMatrix);
	gl.uniformMatrix4fv(programInfo.uniformLocations.modelViewMatrix, false, modelViewMatrix);
	gl.uniform1f(programInfo.uniformLocations.time, time);

	const offset = 0;
	const vertexCount = 4;
	gl.drawArrays(gl.TRIANGLE_STRIP, offset, vertexCount);
}

function main() {
	// Get the canvas to draw on
	const canvas = document.querySelector("#time_background");
	// Make canvas full page sized
	var dimension = [document.documentElement.clientWidth, document.documentElement.clientHeight];
	canvas.width = dimension[0]-document.querySelector(".sidebar").style.width;
	canvas.height = dimension[1];

	// Set it for web GL
	const gl = canvas.getContext("webgl");
	if (gl === null) {
		alert("Unable to initialize WebGL. Your browser or machine may not support it.");
		return;
	}

	// Init shaders
	const shaderProgram = initShaderProgram(gl, vertexSource, fragmentSource);
	const programInfo = {
		program: shaderProgram,
		attribLocations: {
			vertexPosition: gl.getAttribLocation(shaderProgram, 'aVertexPosition'),
		},
		uniformLocations: {
			projectionMatrix: gl.getUniformLocation(shaderProgram, 'uProjectionMatrix'),
			modelViewMatrix: gl.getUniformLocation(shaderProgram, 'uModelViewMatrix'),
			time: gl.getUniformLocation(shaderProgram, 'time')
		},
	};
	const buffers = initBuffers(gl);

	// Create render function that calls itself with delay
	var lastTime = 0;
	function render(currentTime) {
		// Update time
		const nowTime = 0.001 * currentTime;
		const delta = nowTime - lastTime;
		lastTime = nowTime;
		// Update canvas to screen dimensions
		var dimension = [document.documentElement.clientWidth, document.documentElement.clientHeight];
		canvas.width = dimension[0]-document.querySelector(".sidebar").style.width;
		canvas.height = dimension[1];
		// Draw calls
		drawScene(gl, programInfo, buffers, nowTime, dimension);
		// Scedule the next draw
		requestAnimationFrame(render);
	}

	// Start rendering
	requestAnimationFrame(render);
}

window.onload = main;
