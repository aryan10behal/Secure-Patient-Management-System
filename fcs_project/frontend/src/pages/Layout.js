import { CssBaseline } from "@mui/material";
import { Outlet } from "react-router-dom";
import Navbar from "../Components/Navbar";

const Layout = () => {
  return <>
    <CssBaseline />
    <Navbar />
    <Outlet />
  </>;
};

export default Layout;