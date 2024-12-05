import {useState, useEffect} from "react"
import {Link} from "react-router-dom"
import { GoogleLogin } from "@react-oauth/google"
import googleLogin from '../services/googleLogin'
import jwtDecode from "jwt-decode"

function Login() {

    const googleResponse = async (response) => {

        const token = response.credential || response.accessToken;
    
        if (token) {
            const googleResponse = await googleLogin(token);
            console.log(googleResponse); 
            console.log(response); 
        } else {
            console.error("No token received from Google response");
        }
    };

    return (

        <div className="login-container">
            <form className="login-form">
                <label htmlFor="login">Nome de usuário:</label>
                    <input name="login"></input>
                <label htmlFor="password">Senha:</label>
                    <input name="password"></input>
                <button type="submit">Entrar</button>
                
                <Link to="/register" className="login-link">Cadastre-se</Link>
                <GoogleLogin
                    onSuccess={googleResponse}
                    onError={() => {
                        console.log('Login Failed');
                    }}
                />

            </form>
        </div>
    )
}

export default Login