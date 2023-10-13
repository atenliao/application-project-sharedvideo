import React, { useEffect, useState } from "react";
import { Switch, Route, useRouteMatch} from "react-router-dom";
import NavBar from "./NavBar";
import GuessNavBar from "./GuessNavBar";
import Login from "../pages/Login";
import ShowVideoRoute from "../pages/ShowVideoRoute";
import CreateVideo from "../pages/CreateVideo";
import UserVideoList from "../pages/UserVideoList";
import AllVideos from "../pages/AllVideos";
import LoginForm from "./LoginForm";
import SignUpForm from "./SignUpForm";
import VideoPost from "../pages/VideoPost";
// import { useRouteMatch } from "react-router-dom/cjs/react-router-dom.min";


function App() {
  const [user, setUser] = useState(null)
  // const [Login, setLogin] = useState(true)
  const match = useRouteMatch()
  const [videos, setVideos] = useState([])
  useEffect(() => {
    fetch("/check_session").then(
      (r) => {
        if (r.ok) {
          r.json().then((user) => setUser(user));
        }
      });
  }, []);
  
  useEffect(()=>{
    fetch('/videos')
      .then((res)=>res.json())
      .then(setVideos)
},[])

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
          <Route path="/videopost/:id" >
          <VideoPost videos={videos}/>
          </Route>
          <Route path="/">
            <AllVideos videos={videos}/>
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
        
          <Route path="/new">
            {console.log('create video')}
            <CreateVideo user={user} />
          </Route>
          <Route path="/uservideo">
          <UserVideoList />
          </Route>
          <Route path="/videopost/:id" >
          <VideoPost videos={videos}/>
          </Route>
          <Route path="/">
            <AllVideos videos={videos}/>
          </Route>
        </Switch>
      </main>
    </>
  )
}

export default App;


