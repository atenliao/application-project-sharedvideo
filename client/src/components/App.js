import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import NavBar from "./NavBar";
import GuessNavBar from "./GuessNavBar";
import Login from "../pages/Login";
import CreateVideo from "../pages/CreateVideo";
import UserVideoList from "../pages/UserVideoList";
import AllVideos from "../pages/AllVideos";
import LoginForm from "./LoginForm";
import SignUpForm from "./SignUpForm";


function App() {
  const [user, setUser] = useState(null)
  // const [Login, setLogin] = useState(true)

  useEffect(() => {
    fetch("/check_session").then(
      (r) => {
        if (r.ok) {
          r.json().then((user) => setUser(user));
        }
      });
  }, []);
  
  if (!user) return (
    <>
    <GuessNavBar user={user} setUser={setUser} />
    <main>
      <Switch>
          <Route path="/login">
            <LoginForm onLogin={setUser}/>
          </Route>
          <Route path="/signup">
            <SignUpForm onLogin={setUser}/>
          </Route>
           <Route path="/">
            <AllVideos />
          </Route>
      </Switch>
    </main>
    </>
  );

  return (
    <>
      <NavBar user={user} setUser={setUser} />
      <main>
        <Switch>
        <Route path="/">
            <AllVideos />
          </Route>
          <Route path="/new">
            {console.log('create video')}
            <CreateVideo user={user} />
          </Route>
          <Route path="/uservideo">
          <UserVideoList />
          </Route>
        </Switch>
      </main>
    </>
  )
}

export default App;


