import {useState} from "react"
import {Link, useLocation} from "react-router-dom"
import Alocacoes from "./Alocacoes"
import "../styles/Home.css"

function Home() {
    const location = useLocation()
    const { profilePicture } = location.state || {} 
    const [path, setPath] = useState("Alocacoes")

    return (
        <>
            <main className="home-container">
                <div className="menu-container column-container">
                    <img src="./src/images/losango.png" className="menu-logo"/>

                    <hr className="horizontal-line"></hr>
                    <div className="menu-nav">
                        <div className="align-center">
                            <img src="./src/images/losango.png" className="menu-icon"/>
                            <Link className="menu-btn">Alocações</Link>
                        </div>
                        <div className="align-center">
                            <img src="./src/images/losango.png" className="menu-icon"/>
                            <Link className="menu-btn">Locais</Link>
                        </div>
                        <div className="align-center">
                            <img src="./src/images/losango.png" className="menu-icon"/>
                            <Link className="menu-btn">Horários</Link>
                        </div>
                    </div>
                </div>
                <div className="column-container max-width-container">
                    <div className="navbar">
                        <button className="return-btn">
                            <img src="/src/images/left-arrow.png" width="25px" height="25px" />
                        </button>
                        { profilePicture && <img src={profilePicture} className="profile-pic" referrerpolicy="no-referrer"/> }
                    </div>
                    <section className="content-container column-container">

                        {path === "Alocacoes" && <Alocacoes />}

                    </section>
                </div>
            </main>
        </>
    )
}

export default Home