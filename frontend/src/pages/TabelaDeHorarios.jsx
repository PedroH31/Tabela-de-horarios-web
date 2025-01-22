import {useState} from "react"
import {useLocation} from "react-router-dom"

export default function TabelaDeHorarios() {
    const location = useLocation()
    const { alocation } = location.state || {}
    console.log(alocation)
 
    return (
        <div>
            
        </div>
    )

}