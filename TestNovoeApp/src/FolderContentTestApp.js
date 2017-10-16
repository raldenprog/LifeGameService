import React, { Component } from 'react'
import { connect } from 'react-redux'
import * as action from './ActionsTestApp'
import * as types from './ActionTypesTestApp'
import { Components } from './ConstTestApp'

const mapDispatchToProps = (dispatch) => {
  return {
    getDataFolder: (path) => {
      dispatch( action[types.FETCH_METADATA](path) )
    }
  }
}


const mapStateToProps = (state) => {
  return  {
    metadataFolder: state.testApp.currentFolder
  }
}


const WrapFolder = WrappedComponent => {
  class WrappedFolder extends Component {

    componentDidMount = () => {
      this.props.getDataFolder(this.props.location.pathname)
    }

    componentWillReceiveProps = (nextProps) => {
      nextProps.location !== this.props.location
      ? this.props.getDataFolder(nextProps.location.pathname)
      : false
    }

    render() {
      return(
        this.props.metadataFolder !== null
        ? <WrappedComponent {...this.props}/>
        : <div className='alert alert-danger' role='alert'>
          Not data
        </div>)
    }
}
 return connect(mapStateToProps,mapDispatchToProps)(WrappedFolder)
}


const Folder = ({
  metadataFolder: metadataFolder,
  history: history
  }) => (
    <div className='card'>
      <div className='list-group list-group-flush'>
      {metadataFolder._embedded.items.map((el,i) => {
        const Component = Components[el.type]
        return <Component key={i} history={history} params={el}/>
      })}
    </div>
    </div>
  )



const FolderContent = WrapFolder(Folder)
export default FolderContent
