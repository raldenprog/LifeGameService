import React from 'react'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import FolderContent from './FolderContentTestApp'


const Routes = () => (
  <Router>
    <Switch>
      <Route exact path='/' render={ (props) =>
        <FolderContent {...props}/>
      }/>
      <Route path='/:params(.*)' render={ (props) =>
        <FolderContent {...props}/>
      }/>
    </Switch>
  </Router>
)


export default Routes
