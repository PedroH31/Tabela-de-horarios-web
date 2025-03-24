import {Link, useNavigate} from "react-router-dom"
import { GoogleLogin } from "@react-oauth/google"
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants"
import jwtDecode from "jwt-decode"

function Login() {
    const navigate = useNavigate()

    const googleResponse = async (response) => {
        const token = response.credential || response.accessToken
        const apiUrl = import.meta.env.REACT_API_URL

        if (token) {
            console.log("Google token:", token)
            try {
                const backendResponse = await fetch(`http://127.0.0.1:8000/api/google-login/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ token }),
                });

                if (!backendResponse.ok) {
                    console.error("Backend returned an error:", backendResponse.status);
                    const errorData = await backendResponse.json()
                    console.error("Error details:", errorData)
                    return;
                }

                const data = await backendResponse.json()

                if (data.access && data.refresh) {
                    localStorage.setItem(ACCESS_TOKEN, data.access)
                    localStorage.setItem(REFRESH_TOKEN, data.refresh)
                    localStorage.setItem("profilePicture", data.profile_picture)
                    navigate("/")
                }

            } catch (error) {
                console.error("Error during fetch:", error)
            }
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