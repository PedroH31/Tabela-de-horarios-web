import { useState, useEffect } from "react"
import { ACCESS_TOKEN } from '../constants'

export default function Grades() {
    const [addGrade, setAddGrade] = useState(false) 
    const [formData, setFormData] = useState({
        nome: "",
        descricao: "",
        semestre_vigencia: "",
    })

    const toggleAddGrade = () => {
        setAddGrade(true)
    }

    const handleChange = (e) => {
        const { name, value } = e.target
        setFormData(prevFormData => ({
            ...prevFormData,
            [name]: value
        }))
    }

    async function handleSubmit(e) {
        e.preventDefault()

        const token = localStorage.getItem(ACCESS_TOKEN)
        console.log(token)

        try {
            const response = await fetch("http://127.0.0.1:8000/api/grade-curricular/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`
                },
                body: JSON.stringify(formData),
                credentials: 'include'
            }) 

            if (!response.ok) {
                throw new Error("Network response was not ok")
            }

            const data = await response.json()
            console.log("success", data)

            setFormData({
                nome: "",
                descricao: "",
                semestre_vigencia: ""
            })
            
            setAddGrade(false)

        } catch (error) {
            console.error("Error:", error)
        }
    }

    return (
        <>
                <main className="grades-container">
                    <div>
                        <h1>Grades</h1>
                        <div className="align-center search-container">
                            <input className="search-bar"/>
                            <button className="search-btn"><img src="/images/lupa.png" width="25px"/></button>
                        </div>
        
                        <section className="tables-container max-width-container">
                            <button onClick={toggleAddGrade} className="add-btn align-center">
                                <img src="/images/plus-sign.png" className="btn-icon"/>Adicionar</button>
                        </section>
                    </div>
                    {!addGrade ? (
                        <h1>lista de grades</h1>
                        ) :
                        (
                            <div className="individual-alocation-container">
                                <form className="grade-form-container">
                                    <div className="grade-form-element">
                                        <label htmlFor="nome">nome:</label>
                                        <input 
                                            className="grade-form-input" 
                                            name="nome"
                                            value={formData.nome}
                                            onChange={handleChange}
                                        />
                                    </div>
                                    <div className="grade-form-element">
                                        <label htmlFor="descricao">descricao:</label>
                                        <input 
                                            className="grade-form-input" 
                                            name="descricao"
                                            value={formData.descricao}
                                            onChange={handleChange}
                                        />
                                    </div>
                                    <div className="grade-form-element">
                                        <label htmlFor="semestre-vigencia">Vigência:</label>
                                        <input 
                                            className="grade-form-input" 
                                            name="semestre_vigencia"
                                            value={formData.semestre_vigencia}
                                            onChange={handleChange}
                                        />
                                    </div>
                                    <button className="toolbar-btn" type="submit" onClick={handleSubmit}>
                                        <img src="/images/save.png" className="btn-icon"/>
                                    </button>
                                </form>
                            </div>
                        )
                    
                    }
                </main>
            
        </>
    )
}
