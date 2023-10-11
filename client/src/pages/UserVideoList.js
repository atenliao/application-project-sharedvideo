import { useEffect,useState } from "react";
import ReactMarkdown from "react-markdown";
import {Link} from "react-router-dom";
import styled from "styled-components";
import {Box, Button} from "../styles";

function UserVideoList(){
    const [videos, setVideos] =useState([]);

    useEffect(()=>{
        fetch("/videos_userid")
          .then((res) => res.json())
          .then(setVideos);
    },[]);
    return(
        <Wrapper>
            {videos.length > 0 ?(
                videos.map((video)=>(
                    <Video key={video.id}>
                    <Box>
                        <h2>{video.title}</h2>
                        <p>
                            <em>publish at:{video.publish_at}</em>
                            &nbsp;·&nbsp;
                            <cite>By {video}</cite>
                        </p>
                        <ReactMarkdown>{video.views}</ReactMarkdown>
                    </Box>
                </Video>
                ))
            ):(
                <>
                    <h2>No Video Found</h2>
                    <Button as={Link} to="/new">
                        Upload a New Video
                    </Button>
                </>
            )}
        </Wrapper>
    );
}

const Wrapper = styled.section`
  max-width: 800px;
  margin: 40px auto;
`;

const Video = styled.article`
  margin-bottom: 24px;
`;

export default UserVideoList;