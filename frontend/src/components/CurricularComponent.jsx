import { useContext } from "react"
import { ScheduleContext } from "../pages/SchedulesTable"

export default function CurricularComponent(props) {
    const { turma, componente, local, tamanho, cellKey, periodo } = props
    const { editMode } = useContext(ScheduleContext)

    function handleDragStart(e, cellKey, turma, componente, local, tamanho, periodo) {
        const draggedData = JSON.stringify({ cellKey, turma, componente, local, tamanho, periodo })
        e.dataTransfer.setData("application/json", draggedData)
    }

    return (
        
        <div 
        // adicionar local da turma 
            className="curricular-component" 
            draggable={editMode}
            onDragStart={(e) => handleDragStart(e, cellKey, turma, componente, local, tamanho, periodo)}
        >
            <p>{componente}({local})</p>

        </div>
    )
}