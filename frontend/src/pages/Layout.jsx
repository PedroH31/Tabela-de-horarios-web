import {useState, useEffect} from "react"
import {Link, Outlet} from "react-router-dom"
import "../styles/Layout.css"

function Layout() {
    const [profilePicture, setProfilePicture] = useState(null)

    useEffect(() => {
        const storedPicture = localStorage.getItem("profilePicture");
        if (storedPicture) {
          setProfilePicture(storedPicture);
        }
      }, [])

    return (
        <main className="home-container row-container">
            <div className="menu-container column-container">
                <img src="/images/losango.png" className="menu-logo"/>

                <hr className="horizontal-line"></hr>
                <div className="menu-nav">
                    <div className="align-center">
                        <img src="/images/losango.png" className="menu-icon"/>
                        <Link to="/" className="menu-btn">Horarios</Link>
                    </div>
                    <div className="align-center">
                        <img src="/images/losango.png" className="menu-icon"/>
                        <Link className="menu-btn">Locais</Link>
                    </div>
                    <div className="align-center">
                        <img src="/images/losango.png" className="menu-icon"/>
                        <Link to="grades" className="menu-btn">Grades</Link>
                    </div>
                </div>
            </div>
            <div className="main-container column-container max-width-container">
                <div className="navbar">
                    <button className="return-btn">
                        <img src="/images/left-arrow.png" width="25px" height="25px" />
                    </button>
                    { profilePicture && <img src={profilePicture} className="profile-pic" referrerPolicy="no-referrer"/> }
                </div>
                <section className="content-container column-container">
                    <Outlet />
                </section>
            </div>
        </main>

    )
}

export default Layout