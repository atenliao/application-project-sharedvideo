import React, { useState } from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";
import { Button } from "../styles";


function GuessNavBar({ user, setUser }) {
    const [userLogin, setUserLogin] = useState(false)
   
    return (
        <Wrapper>
            <Logo>
                <Link to="/">OTATO.xyz</Link>
            </Logo>
            <Nav>
                {
                    <>
                        <Button as={Link} to="/login" onClick={() => setUserLogin(true)}>
                            Login
                        </Button>
                        <Button as={Link} to="/signup" onClick={() => setUserLogin(false)}>Sign Up</Button>
                    </>
                }


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

export default GuessNavBar;
