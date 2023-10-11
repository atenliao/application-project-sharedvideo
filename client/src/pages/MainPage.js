import React from "react";
import {Route,useRouteMatch} from "react-router-dom"
import AllVideos from "./AllVideos";


function MainPage({videos}){
    const match = useRouteMatch();

    return (<div>
        <AllVideos />
    </div>)


}