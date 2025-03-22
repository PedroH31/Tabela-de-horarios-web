import TableCell from "./TableCell"

export default function TableContainer({ title, slots, schedule, days, tablePeriod }) {
    return (
        <section>
            <div className="table-container">
                {tablePeriod === 1 && (
                    <div className="table-title justify-center">
                        <h2>{title}</h2>
                    </div>
                )}
                {/* table-headers */}
                <div className="table-row">
                    <div className="table-time-slot"></div>
                    {days.map((day, index) => (
                        <div key={day} className="table-header"><p>{day}</p></div>
                    ))}
                </div>
                {/* Table Rows */}
                {slots.map((slot) => (
                    <div key={slot} className="table-row">
                        <div className="table-time-slot"><p>{slot}</p></div>
                        {days.map((day, index) => {
                            const cellKey = `${index + 2}_${slot}`

                            return (
                                <TableCell 
                                    key={cellKey} 
                                    cellKey={cellKey} 
                                    data={schedule[cellKey] || []}
                                    tablePeriod={tablePeriod}
                                />
                            )
                        })}
                    </div>
                ))}
            </div>
        </section>
    )
}