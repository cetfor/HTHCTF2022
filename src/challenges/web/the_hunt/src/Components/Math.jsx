import React from 'react'
import { useState } from 'react'

export default function Math() {

    const[num, setNum] = useState()
    const[math, setMath] = useState("")

    const doMath = (e) => {
        if (e === "add") {
            setMath(`${num} + 5`)
            setNum(num + 5)
        } else if (e === "multi") {
            setMath(`${num} * 5`)
            setNum(num * 5)
        } else {
            setMath("")
            setNum(0)
        }
    }

  return (
    <>
    <h1>{math} {math ? "=" : "Click on the Buttons"} {num ? num : " "}</h1>
    <button onClick={() => doMath("add")}>+</button>
    <button onClick={() => doMath("multi")}>x</button>
    <button onClick={() => doMath("clear")}>Clear</button>
    </>
  )
}

