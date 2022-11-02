import React,  { useState } from 'react'
import Recs from './Recs';

function Skull() {
    
    let passWord = false;
    const [message, setMessage] = useState('Where is the flag!')

    const setCookieFunction = (value) => {
        localStorage.setItem('users', value)
        document.cookie = 'user='+ value;
        setMessage('maybe. . . ')
    }
    
    let cookieValue = document.cookie
    .split(';')
    .find((row) => row.startsWith('user='))
    ?.split('=')[1];
    const value = 'aGFja2luZ19pc19mdW4';
    if (cookieValue === value){
        passWord = true;
    }
    
    if (!passWord) {
        return (
            <>
            <div className='skull' >
            <span>Enter Password:  </span>
            <input type="text" 
            onChange={(e) => setCookieFunction(e.target.value)}></input>
            <p style={{
                fontWeight: 'bold',
                color: 'red',
                opacity: '.5'
            }}>{message}</p>
            <img  src='/img/404_image.png' alt="skulls" />
            <h1>404 Access Denied</h1>
            <p>look at your local storage</p>
            </div>
            </>
        )
    }
    if (passWord === true){
        return (
            <Recs />
        )
    }
}

export default Skull;