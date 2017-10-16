/*
 *XHRProvider for the XHR request
*/
let instance = null

export default class XHRProvider {

  constructor() {
    if (instance !== null) {
      return instance
    }

    this._headerMap_ = {
      json: {'Content-Type': 'application/json'},
      text: {'Content-Type': 'text/html'},
      jpeg: {'Content-Type': 'image/jpeg'},
      png: {'Content-Type': 'image/png'},
    }
  }

  rqInit = (requestMethod, requestHeaders, bodyData) => {
    if (requestMethod === undefined) requestMethod = 'POST'
    if (requestHeaders === undefined) requestHeaders = 'json'
    if (!requestMethod.match(/^(POST|GET|PUT)$/i)) {
      throw new Error(
        `Selected request method: ${requestMethod}. not supported`
      )
    }
    if (this._headerMap_[requestHeaders.toLowerCase()] === undefined) {
      throw new Error(
        `Selected request Content-Type: [:${requestHeaders}:]. Not supported `
      )
    }
    return ({
      method: requestMethod.toUpperCase(),
      headers: this._headerMap_[requestHeaders.toLowerCase()],
      body: bodyData,
    })
  }

  askAPI = (data) => {
    const body = JSON.stringify(data)
    return (
      fetch(new Request('/akka/api/', this.rqInit('POST', 'json', body)))
      .then((response)=>{
        if (response.status === 200) {
          return response.json()
        } else {
          return new Error(
            `Failed to fetch query ${data}, stausCode: ${response.statusText}`
          )
        }
      })
    .then((json)=> {
      return json
    })
    .then((error)=> {
      return error
    })
    )
  }

  getUUID(login, password, atb) {
    if (
      typeof(login) !== 'string'
      && typeof(password) !== 'string'
    ) {
      throw new Error(`Invalid argument exception.
        [:login:]     -> ${typeof(login)} shuld be [string]
        [:password:]  -> ${typeof(password)} shuld be [string]`)
    }
    const body = JSON.stringify({
      p_action: 'uuid',
      params: {login: login, password: password},
    })
    return (
      fetch(new Request('http://172.20.9.22:9008', this.rqInit('POST', 'json', body)))
        .then((response) => {
        if (response.status !== 200) {
          throw new Error(`Failed to exec query. ${response.statusText}`)
        }
        return response.json()
      }
    ))
  }
}
