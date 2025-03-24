import CurricularComponent from "./CurricularComponent"
import { useState, useContext } from "react"
import { ScheduleContext } from "../pages/SchedulesTable"

export default function TableCell({ cellKey, tablePeriod, data }) {
    const [isDraggedOver, setIsDraggedOver] = useState(false)
    const { alocation, setAlocation } = useContext(ScheduleContext)
    const styles = isDraggedOver ?
        { border: "1.5px solid #eeef20" } :
        { border: "1.5px solid black" }

    const handleDragOver = (e) => {
        e.preventDefault()
        setIsDraggedOver(true)
    }

    const handleDragLeave = () => {
        setIsDraggedOver(false)
    }

    const handleDrop = (e) => {
        e.preventDefault()
        setIsDraggedOver(false)

        const draggedData = JSON.parse(e.dataTransfer.getData("application/json"))
        const { cellKey: oldCellKey, turma, componente, local, tamanho, periodo: oldPeriodo } = draggedData
        
        if (oldCellKey === cellKey && oldPeriodo === tablePeriod) return

        const newDistribuicao = { ...alocation.distribuicao }
        
        const sameLocation = newDistribuicao[cellKey]?.some(
            (item) => item.local === local && item.periodo === tablePeriod
        );

        if (sameLocation){
            alert("Mais de um componente curricular possui o mesmo local")

            return
        }

        // Remove from old cell
        newDistribuicao[oldCellKey] = newDistribuicao[oldCellKey].filter(
          (item) => !(item.componente === componente && item.turma === turma && item.periodo === oldPeriodo)
        );
    
        // Add to new cell
        if (!newDistribuicao[cellKey]) newDistribuicao[cellKey] = []
        newDistribuicao[cellKey].push({
          turma,
          componente,
          local,
          tamanho,
          periodo: tablePeriod,
        })
        
        setAlocation({ ...alocation, distribuicao: newDistribuicao })
        
    }

    const filteredData = data.filter((item) => item.periodo === tablePeriod)

    return (
        <div
            className="table-cell"
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
            style={styles}
        >
            {filteredData.length > 0 ? (
                filteredData.map((item, index) => (
                    <CurricularComponent 
                        key={index} 
                        cellKey={cellKey} 
                        {...item} />
                ))
            ) : (
                <div className="empty-cell"></div>
            )}
        </div>
    )
}