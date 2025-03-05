import CurricularComponent from "./CurricularComponent"
import { useState } from "react"
import { useContext } from "react"
import { ScheduleContext } from "../pages/TabelaDeHorarios"

export default function TableCell({ cellKey, data }) {
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
        const { cellKey: oldCellKey, turma, componente, local, tamanho } = draggedData // lembrete: cellKey: oldCellKey está somente renomeando a variável para oldCellKey

        if (oldCellKey === cellKey) return

        const newDistribuicao = alocation.distribuicao.map((entry) => {
            const key = Object.keys(entry)[0]

            if (key === oldCellKey) {
                return { [key]: entry[key]?.filter(item => item.componente !== componente) }
            }

            if (key === cellKey) {
                return { [key]: [...(entry[key] || []), { turma, componente, local, tamanho }] }
            }

            return entry
        })

        if (!newDistribuicao.some(entry => Object.keys(entry)[0] === cellKey)) {
            newDistribuicao.push({ [cellKey]: [{ turma, componente, local, tamanho }] });
        }

        const cleanedDistribuicao = newDistribuicao.filter(entry => {
            const key = Object.keys(entry)[0]
            return entry[key].length > 0
        })

        setAlocation({ ...alocation, distribuicao: cleanedDistribuicao })
    }

    return (
        <div
            className="table-cell"
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
            style={styles}
        >
            {data.length > 0 ? (
                data.map((item, index) => (
                    <CurricularComponent
                        key={index}
                        cellKey={cellKey}
                        {...item}
                    />
                ))
            ) : (
                <div className="empty-cell"></div>
            )}
        </div>
    )
}