import os

from server import Server

server = Server()

@server.get('/')
async def root(request):
    admin = request.cookies.get('admin', '')

    headers = {}
    if admin == '':
        headers['set-cookie'] = 'admin=false'

    if admin == 'true':
        return (200, '''
            <title>Admins Only</title>
            <link rel="stylesheet" href="/style.css" />
            <div class="container">
                <h1>Admins Only</h1>
                You're right, I'm so sorry! Please come right in!<br />
                %s
            </div>
        ''' % os.environ.get('FLAG', 'The flag is missing - please inform CTF team!'), headers)
    else:
        return (200, '''
            <title>Admins Only</title>
            <link rel="stylesheet" href="/style.css" />
            <div class="container">
                <h1>Admins Only</h1>
                I'm so sorry client, you must be an admin to view this content.
            </div>
        ''', headers)


@server.get('/style.css', c_type='text/css')
async def style(request):
    del request
    return (200, '''
        * {
            font-family: 'Helvetica Neue', sans-serif;
            box-sizing: border-box;
        }
        html, body { margin: 0; }
        .container {
            padding: 2rem;
            width: 90%;
            max-width: 900px;
            margin: auto;
        }
        input:not([type="submit"]) {
            width: 100%;
            padding: 8px;
            margin: 8px 0;
        }
    ''')


server.run('0.0.0.0', 7502)
