import {useState, createContext} from "react"
import {useLocation} from "react-router-dom"
import TableCell from "../components/TableCell"
import data from "../data.js"
import "../styles/SchedulesTable.css"

export const ScheduleContext = createContext()

export default function TabelaDeHorarios() {
    const location = useLocation()
    const data = location.state?.data
    const [alocation, setAlocation] = useState(data)
    
    const timeSlots = ["M12", "M34", "M56", "T12", "T34", "T56"]
    const days = ["Seg", "Ter", "Qua", "Qui", "Sex"]
    const scheduleData = {}
    alocation.distribuicao.forEach((entry) => {
        const key = Object.keys(entry)[0]
        scheduleData[key] = entry[key]
    })

    
    return (
        <ScheduleContext.Provider value={{alocation, setAlocation}}>
            <div>
                <section className="table-container">
                    <div className="table-title justify-center">
                        <h2>Proposta - Diurno - 2024.1 - Normal</h2>
                    </div>
                    {/* table-headers */}
                    <div className="table-row">
                        <div className="table-time-slot"></div>
                        {days.map((day, index) => (
                            <div key={day} className="table-header"><p>{day}</p></div>
                        ))}
                    </div>
                    {/* Table Rows */}
                    {timeSlots.map((slot) => (
                        <div key={slot} className="table-row">
                            <div className="table-time-slot"><p>{slot}</p></div>
                            {days.map((day, index) => {
                                const cellKey = `${index + 2}_${slot}` // "2_M12", "3_M34", etc.

                                return (
                                    <TableCell 
                                        key={cellKey} 
                                        cellKey={cellKey} 
                                        data={scheduleData[cellKey] || []}
                                    />
                                )
                            })}
                        </div>
                    ))}

                </section>
            </div>

        </ScheduleContext.Provider>
    )

}