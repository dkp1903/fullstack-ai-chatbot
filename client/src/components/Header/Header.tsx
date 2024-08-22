import React, { Fragment } from "react";
import LinkButton from "../LinkButton";
import "./style.css";
import { HeaderInterface } from "./types";

const Header: React.FC<HeaderInterface> = ({
  mainTitle,
  productTitle,
  ...props
}) => {
  return (
    <Fragment>
      <nav className="app-nav-container">
        <div className="app-nav">
          <a href="https://3500-dkp1903-fullstackaichat-6u5b9d6144f.ws-us115.gitpod.io:4100">{mainTitle}</a>
        </div>
      </nav>

      <div className="nav-link-container">
        <div className="app-nav">
          <h6>{productTitle}</h6>
          <div className="nav-links">
            <LinkButton
              kind={"primary"}
              hasIcon={true}
              text={"Links"}
              href="/"
            />
            <LinkButton
              kind={"secondary"}
              hasIcon={true}
              text={"Collaborate with me"}
              href="/"
            />
          </div>
        </div>
      </div>
    </Fragment>
  );
};

export default Header;
