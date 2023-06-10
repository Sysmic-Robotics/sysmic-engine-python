import React from "react";
import danger from "../assets/danger.svg"
import gear from "../assets/gear.svg"
import logo from "../assets/sysmic.png"

export default function Navbar(){
    const [open, setOpen] = React.useState(false);

    const [emergency, setEmergency] = React.useState({
        isEmergency: false,
        colorEmergency: "not-emergency"
    })

    // Parado de emergencia
    function alarm(){
        setEmergency( prevState => {
            return prevState.isEmergency ? 
            {isEmergency: !prevState, colorEmergency: "not-emergency"} : 
            {isEmergency: !prevState.isEmergency, colorEmergency: "emergency"}
        })
    }

    // Dropdown menu
    const handleOpen = () => {
        setOpen(!open);
    };    

    const navbarStyle = `${emergency.isEmergency ? "bg-emergency" : "bg-electric-blue"} flex h-16 p-4 drop-shadow-lg`
    const dangerSign = `max-h-10 ml-5 cursor-pointer ${emergency.colorEmergency}`

    return(
        <nav className={navbarStyle}>
            <img src={logo}></img>
            <img src={danger} className={dangerSign} onClick={alarm}></img>        
            <div className="ml-auto">
                <button onClick={handleOpen} className="bg-white py-2 px-4 rounded-md w-52">Options</button>  
                {open ? (
                    <ul className="bg-white">
                        <li className="p-3 text-center text-sm">
                            <button>Default</button>
                        </li>
                        <li className="p-3 text-center text-sm">
                            <button>Robot and Ball</button>
                        </li>
                        <li className="p-3 text-center text-sm">
                            <button>Robot, Ball and Goalkeeper</button>
                        </li>
                    </ul>
                ) : null}
            </div>
            <img src={gear} className="max-h-10 ml-10 not-emergency cursor-pointer"></img>
        </nav>
    )
}

// TODO: añadir funcionalidad de menú

/*
    <div className="p-10">
        <a href="#" className="text-white text-3xl font-bold p-3 inline-flex items-center">System Robotics</a>

        <label for="default-toggle" className="inline-flex relative items-center cursor-pointer ml-7">
            <input type="checkbox" value="" id="default-toggle" className="sr-only peer"></input>
            <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-red-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-red-600"></div>
        </label>
    </div>

    <div className="top-nav w-full lg:inline-flex lg:flex-grow lg:w-auto">
        <div className="lg:inline-flex lg:flex-row lg:ml-auto px-2">

            <b id="fps" className="lg:inline-flex lg:w-auto px-3 py-2 rounded text-gray-200">FPS</b>

            <select id="select" className="lg:inline-flex lg:w-auto px-4 py-2 mx-4 rounded">
                <option value="default">Default</option>
                <option value="robot-ball">Robot and Ball</option>
                <option value="robot-ball-goalkeeper">Robot, Ball and Goalkeeper</option>
            </select>
            
            <i className="lg:inline-flex lg:w-auto px-5 py-2 rounded text-gray-200"></i>
        </div>
    </div>

*/

/* el último elemento i tenía el elemento className="fas fa-cog fa-2x" */