import React from 'react';
import './Navbar.css';

import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
//import MenuIcon from '@material-ui/icons/Menu';
import logo from '../../images/Analytica.png';
import { Link } from 'react-router-dom';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
}));

const Navbar = (props) => {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <AppBar position="fixed">
        <Toolbar>
          <IconButton edge="start" className={classes.menuButton} color="Secondary" aria-label="menu">
            {/* <MenuIcon /> */}
          </IconButton>
          <Typography variant="h6" className={classes.title}>
            <img src={logo} className="Navbar-logo" alt="logo"/> | Stock Analytics
          </Typography>
          <Button href="/" color="inherit" size="large">Home</Button>
          <Button href="/explore" color="inherit" size="large">Explore</Button>
          <Button href="/insights" color="inherit" size="large">Insights</Button>
        </Toolbar>
      </AppBar>
    </div>
  );
}

export default Navbar;