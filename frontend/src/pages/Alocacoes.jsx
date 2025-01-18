import "../styles/Alocacoes.css"

export default function Alocacoes() {

    return (
        <>
            <main className="alocacoes-container">
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
            </main>
        </>
    )

}