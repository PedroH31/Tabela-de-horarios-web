export default function CurricularComponent(props) {
    const { componente, local, tamanho } = props

    return (
        <div className="curricular-component">
            <p>{componente}</p>

        </div>
    )
}