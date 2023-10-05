import React from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";
import {Button} from "../styles";


function NavBar({user, setUser}){
    function handleLogout(){
        // fetch("/logout", {
        //     method:"DELETE"})
        //     .then((res) => {
        //         if(res.ok){
        //             setUser(null);
        //         }
        //     });
    }

    return (
        <Wrapper>
            <Logo>
                <Link to="/">OTATO.xyz</Link>
            </Logo>
            <Nav>
                <Button>
                    Upload Video
                </Button>
                <Button variant="outline" onClick={handleLogout}>
                    Logout
                </Button>
            </Nav>
        </Wrapper>
    )

}


const Wrapper = styled.header`
    display:flex;
    justify-content: left;
    align-items: center;
    background:darkorange ;
    padding:8px;
`;

const Logo = styled.h1`
    font-family:"Permanent Marker", cursive;
    font-size: 3rem;
    color: white;
    margin: 0;
    line-height:1;

    a {
        color: inherit;
        text-decoration: none;
    }
`;

const Nav = styled.nav`
    display:flex;
    gap:10px;
    position:absolute;
    right: 10px;
`;

export default NavBar;
