import React from 'react'

function Recs() {
    let username = document.cookie
    .split(';')
    .find((row) => row.startsWith('user='))
    ?.split('=')[0];
    let cookieValue = document.cookie
    .split(';')
    .find((row) => row.startsWith('user='))
    ?.split('=')[1];
    return (
     <>
     <div class="form">
            <form action="/flag2" method="post">
                    <input type="text" name="username" id="username"value={username} />
                    <input type="password" name="password" id="password" value={cookieValue} />
                    <input type="submit" value="Get Flag!"></input>
            </form>
        </div>
     </>
    )
}
export default Recs