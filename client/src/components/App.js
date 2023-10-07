import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import NavBar from "./NavBar";
import Login from "../pages/Login";
import CreateVideo from "../pages/CreateVideo";
import VideoList from "../pages/VideoList";

function App() {
  const [user, setUser] = useState(null)
  
  useEffect(()=>{
    fetch("/check_session").then(
      (r)=>{
        if (r.ok) {
          r.json().then((user) => setUser(user));
        }
      });
  }, []);
  
  if (!user) return <Login onlogin={setUser}/>;

  return (
    <>
      <NavBar user = {user}  setUser={setUser}/>
      <main>
        <Switch>
          <Route path="/new">
            <CreateVideo user={user}/>
          </Route>
          <Route path="/">
            <VideoList />
          </Route>
        </Switch>
      </main>
    </>
  )
}

export default App;


