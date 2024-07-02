import React from "react"
import Field from "../components/Field"
import Navbar from "../components/Navbar"
import Robots from "../components/Robots"

function App() {
  
  return (
    <div className="main">
      <Navbar />
      <div className="flex h-[calc(100vh-64px)]">
        <Robots />
        <Field />
      </div>
    </div>
  )
}

export default App
