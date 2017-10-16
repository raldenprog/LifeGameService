import React, { PropTypes, Component } from 'react'

export default class Req extends Component {
  render() {
    const { req } = this.props
    return <div className='req'>
      <p>НАКОНЕЦ, {name}!</p>
    </div>
  }
}

Req.propTypes = {
  name: PropTypes.string.isRequired
}
