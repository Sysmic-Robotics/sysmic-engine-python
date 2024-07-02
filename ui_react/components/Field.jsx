import React from "react";

function Field(){

    //TODO: agregar movimiento de robots

    function draw() {
		let canvas = this.shadowRoot.getElementById("canvas");
		let ctx = canvas.getContext('2d');

		// Clear
		ctx.clearRect(0, 0, canvas.width, canvas.height);

		// Draw Ai specif stuff
		if (Data.aiEnvironment.name == "default") {
			for (let destination of Data.aiEnvironment.robotDestinations) {
				ctx.beginPath();
				ctx.save();
				ctx.fillStyle = "red";
				ctx.arc(destination.x, destination.y, 2, 0, 2 * Math.PI);
				ctx.fill();
				ctx.restore();
			}
		}

		// Draw ball
		ctx.beginPath();
		ctx.fillStyle = "orange";
		ctx.arc(Data.ball.x, Data.ball.y, 2.15, 0, 2 * Math.PI, false);
		ctx.fill();

		// Draw blue robots
		for (let robot of Data.blue_robots) {
			if (robot.selected) {
				ctx.save();
				ctx.fillStyle = "rgba(62, 161, 240, 0.5)";
				ctx.beginPath();
				ctx.arc(robot.x, robot.y, robot.radius + 10, 0, 2 * Math.PI);
				ctx.fill();
				ctx.restore();
			}

			// Draw robot velocity
			ctx.beginPath();
			ctx.save();
			ctx.strokeStyle = "red";
			ctx.moveTo(robot.x, robot.y);
			ctx.lineTo(robot.x + 60 * robot.velX, robot.y + 60 * robot.velY);
			ctx.stroke();
			ctx.restore();

			// Draw orientation
			ctx.beginPath();
			ctx.save();
			ctx.strokeStyle = "white";
			ctx.lineWidth = 4;
			ctx.arc(robot.x, robot.y, robot.radius + 1, robot.orientation + 0.3, robot.orientation - 0.3, true);
			ctx.stroke();
			ctx.restore();

			// Draw robot
			ctx.beginPath();
			ctx.fillStyle = "#3399ff";
			ctx.arc(robot.x, robot.y, robot.radius, 0, 2 * Math.PI);
			ctx.fill();
			ctx.stroke();

			ctx.beginPath();
			ctx.font = "bold 16px Arial";
			ctx.fillStyle = "black";
			ctx.fillText(`${robot.id}`, robot.x - 4.5, robot.y + 6);

		}

		for (let robot of Data.yellow_robots) {
			ctx.beginPath();
			ctx.save();
			ctx.strokeStyle = "white";
			ctx.lineWidth = 4;
			ctx.arc(robot.x, robot.y, robot.radius + 1, robot.orientation + 0.3, robot.orientation - 0.3, true);
			ctx.stroke();
			ctx.restore();

			ctx.beginPath();
			ctx.fillStyle = "gold";
			ctx.arc(robot.x, robot.y, robot.radius, 0, 2 * Math.PI);
			ctx.fill();
			ctx.stroke();

			ctx.beginPath();
			ctx.font = "bold 16px Arial";
			ctx.fillStyle = "black";
			ctx.fillText(`${robot.id}`, robot.x - 4.5, robot.y + 6);
		}
	}

    return(
        <div id="container" className="p-3">
            <object data="../assets/field.svg" type="image/svg+xml" className="max-w-fit"></object>	
            <canvas className="w-full max-h-[calc(100vh-64px)]" id="canvas" width="960" height="660" ></canvas>
        </div>
    )
}

export default Field