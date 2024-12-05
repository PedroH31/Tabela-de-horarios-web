import {Link} from "react-router-dom"

function Register() {
    return (
        <div className="login-container">
            <form className="login-form">
                <label htmlFor="login">Nome de usuário:</label>
                    <input name="login"></input>
                <label htmlFor="password">Senha:</label>
                    <input name="password"></input>
                <label htmlFor="password">Confirme a senha:</label>
                    <input name="password"></input>
                <button type="submit">Entrar</button>
                
                <Link to="/register" className="login-link">Cadastre-se</Link>

            </form>
        </div>
    )
}

export default Register