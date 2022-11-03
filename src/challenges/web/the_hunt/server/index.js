const path = require("path");
const express = require("express");
const app = express(); 
// const helmet = require("helmet");
const cookieParser = require('cookie-parser');
const jwt = require('jsonwebtoken');
const fs = require("fs");
// const { CLIENT_RENEG_LIMIT } = require("tls");

// app.use(helmet());
app.use(cookieParser());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use(express.static(path.join(__dirname, "..", "build")));
app.use("/0", (req, res, next) => {
  res.sendFile(path.join(__dirname, "..", "build", "index.html"));
});
app.use(express.static(path.join(__dirname,"..",'server', "views")));

app.post("/flag2", (req, res) => {
  let { username, password } = req.body;

  let userdetails = {
    username: "user",
    password: "aGFja2luZ19pc19mdW4",
  };

  if (
    username === userdetails["username"] &&
    password === userdetails["password"]
  ) {
    return res.redirect("/flag22agw4tsdrhsg5y4sdfhs4");
  } else {
    return res.redirect("/0/skull");
  }
})

app.get('/flag22agw4tsdrhsg5y4sdfhs4', (req, res) => {
  res.send("hth{local_storage_is_fun!}")
})

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

app.get("/1", (req, res, next) => {
  let username = req.cookies.username;
  return res.render("home", {
    username,
  })
});

app.get("/login", (req, res) => {
  let bad_auth = req.query.msg ? true : false;

  if (bad_auth) {
    return res.render("login", {
      error: "Invalid username or password",
    });
  } else {
    return res.render("login");
  }
});

app.get("/welcome", (req, res) => {
  let username = req.cookies.username;

  return res.render("welcome", {
    username,
  });
});

app.post("/process_login", (req, res) => {
  let { username, password } = req.body;

  let userdetails = {
    username: "user",
    password: "aGFja2luZ19pc19mdW4",
  };

  if (
    username === userdetails["username"] &&
    password === userdetails["password"]
  ) {
    res.cookie("username", username);
    return res.redirect("/welcome");
  } else {
    return res.redirect("/login?msg=fail");
  }
});

app.get("/logout", (req, res) => {
  res.clearCookie("username");
  return res.redirect("/login");
});

app.get('/ship', (req, res, next) => {
    let getToken = req.cookies;
    getToken = Object.values(getToken);
    var makeToken = jwt.sign({user: 'super_admin', time: Date(), userId: 12}, 'chunk');
   
    if (getToken === ' ') {
    console.log("user has token")
    } else {
      res.cookie("token", makeToken)
    } 
    next (res.render("signUp"))
});

app.post("/jwt", (req, res) => {
  let { username, secret } = req.body;

  let userdetails = {
    username: "super_admin",
    secret: "chunk",
  };

  if (
    username === userdetails["username"] &&
    secret === userdetails["secret"]
  ) {
    return res.send("hth{hashcat_is_fast}  /lk23jrlkgrjg");
  } else {
    return res.redirect("/login?msg=fail");
  }
});


function authenticateToken(req, res) {
  // res.clearCookie(req.params.user);
  // res.clearCookie("username");
  let tokenHeaderKey = req.cookies;
  tokenHeaderKey = Object.values(tokenHeaderKey).toString();
  console.log(tokenHeaderKey)
 
    let jwtSecretKey = 'lk23jrlkgrjg';
  
    try {
        const verified = jwt.verify(tokenHeaderKey, jwtSecretKey);
        if(verified){
            return res.send("hth{JWT_are_a_bit_more_s3cur3!}")
        }else{
            // Access Denied
            return res.status(401);
        }
    } catch (error) {
        // Access Denied
        return res.status(401).send(error).send(tokenHeaderKey);
    }
}

app.get('/lk23jrlkgrjg', authenticateToken, (req, res) => {
});

app.get('/directory', (req, res) => {

  let file = req.query.file
  if (file){
    let render = fs.readFileSync(file)
    res.send(render)
  } else {
    res.redirect('/something');
  }
});

app.get('/something', (req, res) => {
  res.render("directoryTraversal")
})

app.listen(7504, () => {
  console.log("server started");
});