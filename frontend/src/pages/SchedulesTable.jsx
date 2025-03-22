import { useState, createContext } from "react";
import { useLocation } from "react-router-dom";
import TableContainer from "../components/TableContainer.jsx";
import "../styles/SchedulesTable.css";

export const ScheduleContext = createContext();

export default function SchedulesTable() {
    const location = useLocation();
    const data = location.state?.data;
    const [alocation, setAlocation] = useState(data);
    const [editMode, setEditMode] = useState(false);
    const editStyles = editMode 
        ? { border: "2px solid #ffba08" } 
        : { border: "2px solid black" };

    const daySlots = ["M12", "M34", "M56", "T12", "T34", "T56"];
    const nightSlots = ["N12", "N34"];
    const days = ["Seg", "Ter", "Qua", "Qui", "Sex"];
    const tablePeriods = [1, 2, 3, 4, 5, 6];
    const daySchedule = {};
    const nightSchedule = {};

    Object.keys(alocation.distribuicao).forEach((cellKey) => {
        const cellData = alocation.distribuicao[cellKey];
        cellData.forEach((item) => {
            if (cellKey.includes("N")) {
                if (!nightSchedule[cellKey]) nightSchedule[cellKey] = [];
                nightSchedule[cellKey].push(item);
            } else {
                if (!daySchedule[cellKey]) daySchedule[cellKey] = [];
                daySchedule[cellKey].push(item);
            }
        });
    });

    function toggleEditMode() {
        setEditMode(prevEditMode => !prevEditMode);
    }

    const renderTables = (slots, schedule) => {
        const title = slots.length === 2 
            ? "Proposta - Noturno - 2024.1" 
            : "Proposta - Diurno - 2024.1";

        return tablePeriods.map((tablePeriod) => (
            <TableContainer 
                key={tablePeriod}
                title={tablePeriod === 1 ? title : ""}
                slots={slots}
                schedule={schedule}
                days={days}
                tablePeriod={tablePeriod}
            />
        ));
    };

    return (
        <ScheduleContext.Provider value={{ alocation, setAlocation, editMode }}>
            <div className="toolbar-container row-container">
                <button onClick={toggleEditMode} className="toolbar-btn" style={editStyles}>
                    <img src="./src/images/edit-button.png" className="btn-icon" />
                </button>
            </div>
            <div className="row-container">
                <div className="column-container">
                    {renderTables(daySlots, daySchedule)}
                </div>
                <div className="column-container">
                    {renderTables(nightSlots, nightSchedule)}
                </div>
            </div>
        </ScheduleContext.Provider>
    );
}