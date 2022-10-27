import React from "react";
import AppRoutes from "./Components/AppRoutes";
import Skulls from "./Components/Skulls";
import "./App.css"

function App() {
  return (
      <>
    <div className="header">
      <img src="/img/headerBackground.png" alt="navbarBg" />
      <ul className="navBar">
        <li><a href="/">{<img src="/img/homeIcon.png" alt="navbarImage" />}</a></li>
        <li><a href="0/skull">{<img src="/img/skull.png" alt="navbarImage" />}</a></li>
        <li><a href="/1">{<img src="/img/skullFireHeaderIcon.png" alt="navbarImage" />}</a></li>
        <li><a href="/ship">{<img src="/img/shipHeader.png" alt="navbarImage" />}</a></li>
      </ul>
    </div>
    <AppRoutes />
    <Skulls />
      </>
  )
}

export default App;