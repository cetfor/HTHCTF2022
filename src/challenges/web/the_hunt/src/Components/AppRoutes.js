import React from "react"
import { BrowserRouter, Routes, Route } from "react-router-dom"
import Home from "./Home.jsx"
import Skull from "./Skull.jsx"

function AppRoutes () {
    return (
        <BrowserRouter>
        <Routes>
            <Route path="/" element={<div><Home/></div>} />
            <Route path="0/skull" element={<div><Skull/></div>} />
        </Routes>
        </BrowserRouter>
    )
}

export default AppRoutes;