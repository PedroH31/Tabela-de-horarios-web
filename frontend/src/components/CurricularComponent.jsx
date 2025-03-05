export default function CurricularComponent(props) {
    const { turma, componente, local, tamanho, cellKey } = props

    function handleDragStart(e, cellKey, turma, componente, local, tamanho) {
        const draggedData = JSON.stringify({ cellKey, turma, componente, local, tamanho })
        e.dataTransfer.setData("application/json", draggedData)
    }

    function handleOnDrop(e) {

    }

    return (
        <div 
            className="curricular-component" 
            draggable
            onDragStart={(e) => handleDragStart(e, cellKey, turma, componente, local, tamanho)}
        >
            <p>{componente}</p>

        </div>
    )
}