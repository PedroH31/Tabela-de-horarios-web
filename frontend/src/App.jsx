import react from "react"
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import Login from "./pages/Login"
import Register from "./pages/Register"
import Layout from "./pages/Layout"
import Horarios from "./pages/Horarios"
import NotFound from "./pages/NotFound"
import ProtectedRoute from "./components/ProtectedRoute"
import { GoogleOAuthProvider } from '@react-oauth/google'
import SchedulesTable from "./pages/SchedulesTable"
import Grades from "./pages/Grades"

function Logout() {
  localStorage.clear()
  return <Navigate to="/login"/>
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

function App() {
  return (
    <GoogleOAuthProvider clientId="186703630780-ugg5qg0siql666tnu3q3tlt1pl29fo2p.apps.googleusercontent.com">
      <BrowserRouter>
        <Routes>
          <Route
            path="/"
            element={
              <ProtectedRoute>
                <Layout />
              </ProtectedRoute>
            }>
          {/* Protected Routes */}
          
            <Route index element={<Horarios />}/>
            <Route path="/tabela-de-horarios" element={<SchedulesTable />}/>
            <Route path="/grades" element={<Grades />}/>
            
          </Route>

          {/* Public routes */}

          <Route path="/login" element={<Login />}/>
          <Route path="/register" element={<RegisterAndLogout />} />
          

          <Route path="*" element={<NotFound />}/>
        </Routes>
      </BrowserRouter>
    </GoogleOAuthProvider>
  )
}

export default App
