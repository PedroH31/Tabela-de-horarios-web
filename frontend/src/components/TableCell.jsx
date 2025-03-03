import CurricularComponent from "./CurricularComponent" 

export default function TableCell({ cellKey, data }) {

    return (
        <div className="table-cell">
            {data.length > 0 ? (
                data.map((item, index) => (
                    <CurricularComponent key={index} {...item} />
                ))
            ) : (
                <div className="empty-cell"></div>
            )}
        </div>
    )
}