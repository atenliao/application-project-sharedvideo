import { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";
import { Link } from "react-router-dom";
import styled from "styled-components";
import {Box, Button} from '../styles';


function AllVideos(){
    const [videos, setVideos] = useState([])

    useEffect(()=>{
        fetch('/videos')
          .then((res)=>res.json())
          .then(setVideos)
    })
    return (
        <Wrapper>
            {videos.map((video)=>(
                    <Video key={video.id}>
                        <h2>{video.title}</h2>
                        <img src={`https://ytimg.googleusercontent.com/vi/${
                            video.video_url.split('v=')[1]}/sddefault.jpg`}
                            alt={video.title}>
                        </img>
                        <p>
                            <em>publish at:{video.publish_at}</em>
                            &nbsp;·&nbsp;
                            <cite>By {video.user.username}</cite>
                        </p>
                        {/* <Link to={`/videos/${video.id}`}>Learn more...</Link> */}
                        {/* <ReactMarkdown>{video.views}</ReactMarkdown> */}
                </Video>
                ))
            }
        </Wrapper>
    )
}

const Wrapper = styled.section`
  max-width: 800px;
  margin: 40px auto;
`;

// const Cards = styled.div`
//     display:grid;
//     grid-template-columns: repeat(auto-fit, minmax(250px,1fx));
//     grid-gap:2rem;
// `

const Video = styled.article`
  margin-bottom: 24px;
`;

export default AllVideos;