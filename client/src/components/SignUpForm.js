import React, {useState} from "react";
import {Button, Error, Input, FormField, Label } from "../styles";

function SignUpForm({onLogin}) {
    const [usename, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [passwordConfirm, setPasswordConfirm] = useState("");
    const [imageUrl, setImageUrl] = useState("");
    const [error, setError] =useState([])
    const [isLoading,setIsLoading] = useState(false);

    function handleSubmit(e){
        e.preventDefault();
        setError([]);
        setIsLoading(true);
        fetch("/sigup",{
            method: "POST",
            headers: {
                "Content-Type":"application/json",
            },
            body: JSON.stringify({
                username,
                password,
                password_confirm: passwordConfirm,
                image_url: imageUrl,
            }),
        }).then((res)=>{
            setIsLoading(false);
            if(res.ok) {
                res.json().then((user)=>onLogin(user));
            }else{
                res.json().then((err) => setError(err.error));
            }
        })
    }

    return (
        <form onSubmit={handleSubmit}>
            <FormField>
                <Label htmlFor="username">Username</Label>
                <Input 
                    type = "text"
                    id="username"
                    autoComplete="off"
                    value={username}
                    onChange={(e)=>setUsername(e.target.value)}
                />
            </FormField>
            <FormField>
                <Label htmlFor="password">Password</Label>
                <Input 
                    type = "password"
                    id = "password"
                    value = {password}
                    onChange={(e)=>setPassword(e.target.value)}
                    autoComplete="current-password"
                />
            </FormField>
            <FormField>
                <label htmlFor="password">Password Confirmation</label>
                <Input 
                    type="password"
                    id = "password"
                    value = {passwordConfirm}
                    onChange={(e)=>setPasswordConfirm(e.target.value)}
                    autoComplete="current-password"
                />
            </FormField>
            <FormField>
                <Label htmlFor="imageUrl">Profile Image</Label>
                <Input 
                    type="text"
                    id="imageUrl"
                    value={imageUrl}
                    onChange={(e)=>setImageUrl(e.target.value)}
                />
            </FormField>
            <FormField>
                <Button type="submit">{isLoading ? "Loading...":"Sign Up"}</Button>
            </FormField>
            <FormField>
                {error.map((err) =>(
                    <Error key={err}>{err}</Error>
                ))}
            </FormField>
        </form>
    )
}