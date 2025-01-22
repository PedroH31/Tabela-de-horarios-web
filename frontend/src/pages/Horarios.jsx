import "../styles/Horarios.css"
import { useState } from "react"
import { Link } from "react-router-dom"
import data from "../data.js"

export default function Horarios() {
    const [alocationsList, setAlocationsList] = useState(data)

    const alocationElements = alocationsList.map(alocation => (
        <div className="individual-alocation-container row-container align-center" key={alocation.id}>
            <p>ECT 2024.1 v1</p>
            <div>
                <Link to="/tabela-de-horarios" state={{alocation}}className="alocation-btn">Visualizar</Link>
                <button className="alocation-btn">Remover</button>
            </div>
        </div>
    ))

    return (
        <>
            <main className="horarios-container">
                <div>
                    <h1>Alocações</h1>
                    <div className="align-center search-container">
                        <input className="search-bar"/>
                        <button className="search-btn"><img src="./src/images/lupa.png" width="25px"/></button>
                    </div>

                    <section className="tables-container max-width-container">
                        <button className="add-btn align-center"><img src="./src/images/plus-sign.png" className="btn-icon"/>Adicionar</button>
                    </section>
                </div>
                {alocationElements}
            </main>
        </>
    )

}