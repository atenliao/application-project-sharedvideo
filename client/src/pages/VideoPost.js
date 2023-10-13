import React, { useState } from "react";
import { useParams } from "react-router-dom";
import { Button, } from "../styles";
import YouTube from 'react-youtube'

function VideoPost({ videos }) {
    const [player, setPlayer] = useState(null);
    // const [video, setVideo] = useState(null)
    const params = useParams(); 
    if (videos.length > 0 ){ 
        const post= videos.find((videoItem) => videoItem.id==params.id)
        const youtubeID = post.video_url.split('v=')[1];
        const onReady = (e) => {
            setPlayer(e.target);
        }
        return (
                <div>
                    <h3>{post.title}</h3>
                    <div>
                        <YouTube 
                            videoId = {youtubeID}
                            onReady = {onReady}
                            opts={{
                                playerVars: {
                                   controls: 0,
                                }
                            }}
                        />
                    </div>
                </div>
            
        );
    }
    

}

export default VideoPost;